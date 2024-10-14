const Admin = require('../models/adminModel');
const bcrypt = require('bcryptjs');
// You'll need to implement or mock these services for other microservices
const userService = require('./userService');
const restaurantService = require('./restaurantService');
const orderService = require('./orderService');
const deliveryService = require('./deliveryService');

exports.authenticateAdmin = async (email, password) => {
  const admin = await Admin.findOne({ email });
  if (admin && await bcrypt.compare(password, admin.password)) {
    return admin;
  }
  return null;
};

exports.createAdmin = async (adminData) => {
  const admin = new Admin(adminData);
  return await admin.save();
};

exports.getAllUsers = async () => {
  return await userService.getAllUsers();
};

exports.getAllRestaurants = async () => {
  return await restaurantService.getAllRestaurants();
};

exports.getAllOrders = async () => {
  return await orderService.getAllOrders();
};

exports.getAllDeliveries = async () => {
  return await deliveryService.getAllDeliveries();
};