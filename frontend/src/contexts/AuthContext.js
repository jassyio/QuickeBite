import React, { createContext, useState, useEffect } from 'react';
import { login, register, logout } from '../services/authService';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if there's a token in localStorage
    const token = localStorage.getItem('token');
    if (token) {
      // TODO: Implement a function to validate the token and get user info
      // For now, we'll just set a dummy user
      setUser({ id: '1', name: 'John Doe' });
    }
    setLoading(false);
  }, []);

  const loginUser = async (email, password) => {
    try {
      const data = await login(email, password);
      localStorage.setItem('token', data.token);
      setUser(data.user);
      return data.user;
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  };

  const registerUser = async (username, email, password) => {
    try {
      const data = await register(username, email, password);
      localStorage.setItem('token', data.token);
      setUser(data.user);
      return data.user;
    } catch (error) {
      console.error('Registration failed:', error);
      throw error;
    }
  };

  const logoutUser = () => {
    localStorage.removeItem('token');
    setUser(null);
    logout(); // Call the logout service if you have one
  };

  return (
    <AuthContext.Provider value={{ user, loading, loginUser, registerUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
};