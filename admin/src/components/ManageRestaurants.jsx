import React, { useState, useEffect } from 'react';
import { getRestaurants, updateRestaurant, deleteRestaurant } from '../services/adminService';

function ManageRestaurants() {
    const [restaurants, setRestaurants] = useState([]);
  
    useEffect(() => {
      fetchRestaurants();
    }, []);
  
    const fetchRestaurants = async () => {
      try {
        const data = await getRestaurants();
        setRestaurants(data);
      } catch (error) {
        console.error('Failed to fetch restaurants:', error);
      }
    };
  
    const handleUpdateRestaurant = async (id, restaurantData) => {
      try {
        await updateRestaurant(id, restaurantData);
        fetchRestaurants();
      } catch (error) {
        console.error('Failed to update restaurant:', error);
      }
    };
  
    const handleDeleteRestaurant = async (id) => {
      try {
        await deleteRestaurant(id);
        fetchRestaurants();
      } catch (error) {
        console.error('Failed to delete restaurant:', error);
      }
    };
  
    return (
      <div>
        <h2>Manage Restaurants</h2>
        <ul>
          {restaurants.map(restaurant => (
            <li key={restaurant.id}>
              {restaurant.name}
              <button onClick={() => handleUpdateRestaurant(restaurant.id, { /* updated data */ })}>Update</button>
              <button onClick={() => handleDeleteRestaurant(restaurant.id)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default ManageRestaurants;