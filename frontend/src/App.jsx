import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Auth/Login';
import RestaurantList from './components/Restaurant/RestaurantList';
import OrderForm from './components/Order/OrderForm';
import DeliveryTracker from './components/Delivery/DeliveryTracker';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/restaurants" component={RestaurantList} />
          <Route path="/order" component={OrderForm} />
          <Route path="/track" component={DeliveryTracker} />
          <Route path="/" exact component={RestaurantList} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;