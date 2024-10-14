const adminService = require('../services/adminService');
const jwt = require('jsonwebtoken');

exports.login = async (req, res) => {
  try {
    const { email, password } = req.body;
    const admin = await adminService.authenticateAdmin(email, password);
    if (admin) {
      const token = jwt.sign({ id: admin._id, role: admin.role }, process.env.JWT_SECRET, { expiresIn: '1h' });
      res.json({ token, admin: { id: admin._id, username: admin.username, role: admin.role } });
    } else {
      res.status(401).json({ message: 'Invalid credentials' });
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

exports.register = async (req, res) => {
  try {
    const admin = await adminService.createAdmin(req.body);
    res.status(201).json(admin);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

exports.getAllUsers = async (req, res) => {
  try {
    const users = await adminService.getAllUsers();
    res.json(users);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

exports.getAllRestaurants = async (req, res) => {
  try {
    const restaurants = await adminService.getAllRestaurants();
    res.json(restaurants);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

exports.getAllOrders = async (req, res) => {
  try {
    const orders = await adminService.getAllOrders();
    res.json(orders);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

exports.getAllDeliveries = async (req, res) => {
  try {
    const deliveries = await adminService.getAllDeliveries();
    res.json(deliveries);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};