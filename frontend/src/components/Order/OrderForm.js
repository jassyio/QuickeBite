import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { getRestaurantById } from '../../services/restaurantService';
import { createOrder } from '../../services/orderService';
import Hero from '../Hero';
import './OrderForm.css';

function OrderForm() {
  const [restaurant, setRestaurant] = useState(null);
  const [orderItems, setOrderItems] = useState([]);
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    const restaurantId = new URLSearchParams(location.search).get('restaurantId');
    async function fetchRestaurant() {
      try {
        const data = await getRestaurantById(restaurantId);
        setRestaurant(data);
        setOrderItems(data.menu.map(item => ({ ...item, quantity: 0 })));
      } catch (error) {
        console.error('Failed to fetch restaurant:', error);
      }
    }
    fetchRestaurant();
  }, [location]);

  const handleQuantityChange = (index, value) => {
    const newOrderItems = [...orderItems];
    newOrderItems[index].quantity = Math.max(0, value);
    setOrderItems(newOrderItems);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const items = orderItems.filter(item => item.quantity > 0);
    try {
      const order = await createOrder({
        restaurantId: restaurant.id,
        items: items.map(item => ({
          name: item.name,
          quantity: item.quantity,
          price: item.price
        })),
        totalAmount: items.reduce((total, item) => total + item.price * item.quantity, 0)
      });
      navigate(`/track?orderId=${order.id}`);
    } catch (error) {
      console.error('Failed to create order:', error);
    }
  };

  return (
    <Hero title="Place Your Order">
      <div className="order-form-container">
        {restaurant ? (
          <>
            <h2>{restaurant.name}</h2>
            <form onSubmit={handleSubmit}>
              {orderItems.map((item, index) => (
                <div className="order-item" key={item.id}>
                  <span>{item.name} - ${item.price}</span>
                  <input
                    type="number"
                    value={item.quantity}
                    onChange={(e) => handleQuantityChange(index, parseInt(e.target.value))}
                    min="0"
                  />
                </div>
              ))}
              <button type="submit" className="order-button">Place Order</button>
            </form>
          </>
        ) : (
          <div className="loading-placeholder" /> 
        )}
      </div>
    </Hero>
  );
}

export default OrderForm;
