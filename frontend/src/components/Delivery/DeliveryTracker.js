import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { getOrderStatus } from '../../services/deliveryService';
import Hero from '../Hero'; // Import Hero component
import './DeliveryTracker.css'; // Import the CSS file for styling

function DeliveryTracker() {
  const [status, setStatus] = useState('');
  const location = useLocation();

  useEffect(() => {
    const orderId = new URLSearchParams(location.search).get('orderId');
    async function fetchOrderStatus() {
      try {
        const data = await getOrderStatus(orderId);
        setStatus(data.status);
      } catch (error) {
        console.error('Failed to fetch order status:', error);
      }
    }
    fetchOrderStatus();
    const interval = setInterval(fetchOrderStatus, 30000); // Update every 30 seconds
    return () => clearInterval(interval);
  }, [location]);

  return (
    <Hero title="Track Your Order"> {/* Wrapping content in Hero */}
      <div className="delivery-tracker-container">
        <h2>Order Status</h2>
        <p>Current status: <span className="status-text">{status}</span></p>
      </div>
    </Hero>
  );
}

export default DeliveryTracker;
