import axios from 'axios';

const API_URL = 'http://localhost:8080/api/admin';

const getAuthHeader = () => {
  const token = localStorage.getItem('adminToken');
  return { Authorization: `Bearer ${token}` };
};

export const login = async (email, password) => {
  const response = await axios.post(`${API_URL}/login`, { email, password });
  return response.data;
};

export const getUsers = async () => {
  const response = await axios.get(`${API_URL}/users`, { headers: getAuthHeader() });
  return response.data;
};

export const updateUser = async (id, userData) => {
  const response = await axios.put(`${API_URL}/users/${id}`, userData, { headers: getAuthHeader() });
  return response.data;
};

export const deleteUser = async (id) => {
  const response = await axios.delete(`${API_URL}/users/${id}`, { headers: getAuthHeader() });
  return response.data;
};

export const getRestaurants = async () => {
  const response = await axios.get(`${API_URL}/restaurants`, { headers: getAuthHeader() });
  return response.data;
};

export const updateRestaurant = async (id, restaurantData) => {
  const response = await axios.put(`${API_URL}/restaurants/${id}`, restaurantData, { headers: getAuthHeader() });
  return response.data;
};

export const deleteRestaurant = async (id) => {
  const response = await axios.delete(`${API_URL}/restaurants/${id}`, { headers: getAuthHeader() });
  return response.data;
};

export const getOrders = async () => {
  const response = await axios.get(`${API_URL}/orders`, { headers: getAuthHeader() });
  return response.data;
};

export const updateOrderStatus = async (id, status) => {
  const response = await axios.put(`${API_URL}/orders/${id}/status`, { status }, { headers: getAuthHeader() });
  return response.data;
};

export const getDeliveries = async () => {
  const response = await axios.get(`${API_URL}/deliveries`, { headers: getAuthHeader() });
  return response.data;
};

export const assignDriver = async (id, driverId) => {
  const response = await axios.put(`${API_URL}/deliveries/${id}/assign`, { driverId }, { headers: getAuthHeader() });
  return response.data;
};