import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ManageUsers from './components/ManageUsers';
import ManageRestaurants from './components/ManageRestaurants';
import ManageOrders from './components/ManageOrders';
import ManageDeliveries from './components/ManageDeliveries';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={Dashboard} />
          <Route path="/users" component={ManageUsers} />
          <Route path="/restaurants" component={ManageRestaurants} />
          <Route path="/orders" component={ManageOrders} />
          <Route path="/deliveries" component={ManageDeliveries} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;