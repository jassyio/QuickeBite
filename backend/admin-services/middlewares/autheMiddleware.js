const jwt = require('jsonwebtoken');

exports.isAdmin = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (token) {
    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET);
      req.user = decoded;
      if (decoded.role === 'admin' || decoded.role === 'super_admin') {
        return next();
      }
    } catch (error) {
      return res.status(401).json({ message: 'Invalid token' });
    }
  }
  return res.status(403).json({ message: 'Access denied' });
};

exports.isSuperAdmin = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (token) {
    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET);
      req.user = decoded;
      if (decoded.role === 'super_admin') {
        return next();
      }
    } catch (error) {
      return res.status(401).json({ message: 'Invalid token' });
    }
  }
  return res.status(403).json({ message: 'Access denied' });
};
