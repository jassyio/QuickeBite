import React from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <nav>
        <ul>
          <li><Link to="/users">Manage Users</Link></li>
          <li><Link to="/restaurants">Manage Restaurants</Link></li>
          <li><Link to="/orders">Manage Orders</Link></li>
          <li><Link to="/deliveries">Manage Deliveries</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Dashboard;