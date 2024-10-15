import React, { useState, useEffect } from 'react';
import { getOrders, updateOrderStatus } from '../services/adminService';

function ManageOrders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const data = await getOrders();
      setOrders(data);
    } catch (error) {
      console.error('Failed to fetch orders:', error);
    }
  };

  const handleUpdateStatus = async (id, status) => {
    try {
      await updateOrderStatus(id, status);
      fetchOrders();
    } catch (error) {
      console.error('Failed to update order status:', error);
    }
  };

  return (
    <div>
      <h2>Manage Orders</h2>
      <ul>
        {orders.map(order => (
          <li key={order.id}>
            Order #{order.id} - Status: {order.status}
            <button onClick={() => handleUpdateStatus(order.id, 'preparing')}>Preparing</button>
            <button onClick={() => handleUpdateStatus(order.id, 'out_for_delivery')}>Out for Delivery</button>
            <button onClick={() => handleUpdateStatus(order.id, 'delivered')}>Delivered</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ManageOrders;