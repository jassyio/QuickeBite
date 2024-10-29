import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Import the CSS file

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // State to track login status

  useEffect(() => {
    const token = localStorage.getItem('token'); // Check for token
    setIsLoggedIn(!!token); // Set login state based on token existence
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token'); // Clear token on logout
    setIsLoggedIn(false); // Update state
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">QuickBite</div>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/restaurants">Restaurants</Link></li>
        <li><Link to="/order">Order</Link></li>
        <li><Link to="/track">Track</Link></li>
        {isLoggedIn ? (
          <li><Link to="/" onClick={handleLogout}>Logout</Link></li>
        ) : (
          <>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/register">Register</Link></li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
