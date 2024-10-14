const Restaurant = require('../models/restaurantModel');

exports.createRestaurant = async (restaurantData) => {
    const restaurant = new Restaurant(restaurantData);
    return await restaurant.save();
};

exports.getAllRestaurants = async () => {
    return await Restaurant.find();
};

exports.getRestaurantById = async (id) => {
    return await Restaurant.findById(id);
};

exports.updateRestaurant = async (id, restaurantData) => {
    return await Restaurant.findByIdAndUpdate(id, restaurantData, { new: true });
};

exports.deleteRestaurant = async (id) => {
    return await Restaurant.findByIdAndDelete(id);
};
