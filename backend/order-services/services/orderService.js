const Order = require('../models/orderModel');

exports.createOrder = async (orderData) => {
    const order = new Order(orderData);
    return await order.save();
}

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
