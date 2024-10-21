import React from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';

export default function Navbar() {
    return (
        <nav className="navbar">
            <li><Link to="/"><h1>QuickBite</h1></Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/signup">Signup</Link></li>
            <li><Link to="/restaurants">Restaurants</Link></li>
            <li><Link to="/orders">Orders</Link></li>
        </nav>
    )
}
