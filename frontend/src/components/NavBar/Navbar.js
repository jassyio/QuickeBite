import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Import the CSS file

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">
        <Link to="/">QuickBite</Link>
      </div>
      <ul>
        <li><Link to="/restaurants">Restaurants</Link></li>
        <li><Link to="/order">Order</Link></li>
        <li><Link to="/track">Track</Link></li>
        <li><Link to="/login">Login</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
