import React, { useState, useEffect } from 'react';
import { getDeliveries, assignDriver } from '../services/adminService';

function ManageDeliveries() {
  const [deliveries, setDeliveries] = useState([]);

  useEffect(() => {
    fetchDeliveries();
  }, []);

  const fetchDeliveries = async () => {
    try {
      const data = await getDeliveries();
      setDeliveries(data);
    } catch (error) {
      console.error('Failed to fetch deliveries:', error);
    }
  };

  const handleAssignDriver = async (id, driverId) => {
    try {
      await assignDriver(id, driverId);
      fetchDeliveries();
    } catch (error) {
      console.error('Failed to assign driver:', error);
    }
  };

  return (
    <div>
      <h2>Manage Deliveries</h2>
      <ul>
        {deliveries.map(delivery => (
          <li key={delivery.id}>
            Delivery #{delivery.id} - Status: {delivery.status}
            {!delivery.driverId && (
              <button onClick={() => handleAssignDriver(delivery.id, /* driver ID */)}>Assign Driver</button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ManageDeliveries;