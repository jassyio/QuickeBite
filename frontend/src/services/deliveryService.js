import axios from 'axios';

const API_URL = 'http://localhost:8080/api/deliveries';

export const getOrderStatus = async (orderId) => {
  const token = localStorage.getItem('token');
  const response = await axios.get(`${API_URL}/status/${orderId}`, {
    headers: { Authorization: `Bearer ${token}` }
  });
  return response.data;
};