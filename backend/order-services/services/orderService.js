const Order = require('../models/orderModel');
const messageBroker = require('../../common/messageBroker');
const { logger } = require('../../common/errorHandler');

exports.createOrder = async (orderData) => {
  try {
    const order = new Order(orderData);
    await order.save();
    
    await messageBroker.publishMessage('order_created', {
      orderId: order._id,
      userId: order.userId,
      restaurantId: order.restaurantId
    });

    return order;
  } catch (error) {
    logger.error('Error creating order', { error });
    throw error;
  }
};

exports.getAllOrders = async () => {
    return await Order.find();
}

exports.getOrderById = async (id) => {
    return await Order.findById(id);
}

exports.updateOrder = async (id, orderData) => {
    return await Order.findByIdAndUpdate(id, orderData, { new: true });
}

exports.deleteOrder = async (id) => {
    return await Order.findByIdAndDelete(id);
}
