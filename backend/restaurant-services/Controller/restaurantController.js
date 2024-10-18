const restaurantService = require('../service/restaurantService');

exports.createRestaurant = async (req, res) => {
    try {
        const restaurant = await restaurantService.createRestaurant(req.body);
        res.status(201).json(restaurant);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

exports.getAllRestaurants = async (req, res) => {
    try {
        const restaurants = await restaurantService.getAllRestaurants();
        res.status(200).json(restaurants);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

exports.getRestaurantById = async (req, res) => {
    try {
        const restaurant = await restaurantService.getRestaurantById(req.params.id);
        res.json(restaurant);
    } catch (error) {
        res.status(404).json({ error: 'Restaurant not found' });
    }
};

exports.updateRestaurant = async (req, res) => {
    try {
        const restaurant = await restaurantService.updateRestaurant(req.params.id, req.body);
        res.json(restaurant);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

exports.deleteRestaurant = async (req, res) => {
    try {
        await restaurantService.deleteRestaurant(req.params.id);
        res.status(204).send();
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

