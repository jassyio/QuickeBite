const express = require('express');
const adminController = require('../controllers/adminController');
const authMiddleware = require('../middleware/authMiddleware');

const router = express.Router();

router.post('/login', adminController.login);
router.post('/register', authMiddleware.isSuperAdmin, adminController.register);
router.get('/users', authMiddleware.isAdmin, adminController.getAllUsers);
router.get('/restaurants', authMiddleware.isAdmin, adminController.getAllRestaurants);
router.get('/orders', authMiddleware.isAdmin, adminController.getAllOrders);
router.get('/deliveries', authMiddleware.isAdmin, adminController.getAllDeliveries);

module.exports = router;