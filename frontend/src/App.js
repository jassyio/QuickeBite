import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import { CartProvider } from './contexts/CartContext';
import Login from './components/Auth/Login';
import RestaurantList from './components/Restaurant/RestaurantList';
import OrderForm from './components/Order/OrderForm';
import DeliveryTracker from './components/Delivery/DeliveryTracker';

function App() {
  return (
    <AuthProvider>
      <CartProvider>
        <Router>
          <div className="App">
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="/restaurants" element={<RestaurantList />} />
              <Route path="/order" element={<OrderForm />} />
              <Route path="/track" element={<DeliveryTracker />} />
              <Route path="/" element={<RestaurantList />} />
            </Routes>
          </div>
        </Router>
      </CartProvider>
    </AuthProvider>
  );
}

export default App;