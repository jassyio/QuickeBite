const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());
app.use(express.json());

// Proxy middleware configuration
const userServiceProxy = createProxyMiddleware({
  target: 'http://localhost:5000',
  changeOrigin: true,
  pathRewrite: {'^/api/users': ''}
});

const restaurantServiceProxy = createProxyMiddleware({
  target: 'http://localhost:3001',
  changeOrigin: true,
  pathRewrite: {'^/api/restaurants': ''}
});

const orderServiceProxy = createProxyMiddleware({
  target: 'http://localhost:3002',
  changeOrigin: true,
  pathRewrite: {'^/api/orders': ''}
});

const deliveryServiceProxy = createProxyMiddleware({
  target: 'http://localhost:5001',
  changeOrigin: true,
  pathRewrite: {'^/api/deliveries': ''}
});

// Routes
app.use('/api/users', userServiceProxy);
app.use('/api/restaurants', restaurantServiceProxy);
app.use('/api/orders', orderServiceProxy);
app.use('/api/deliveries', deliveryServiceProxy);

app.listen(PORT, () => {
  console.log(`API Gateway running on port ${PORT}`);
});