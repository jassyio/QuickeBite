const { spawn } = require('child_process');
const path = require('path');

const services = [
  { name: 'user-service', dir: '../user-services', command: 'python', args: ['run.py'] },
  { name: 'restaurant-service', dir: '../restaurant-services', command: 'npm', args: ['run', 'server'] },
  { name: 'order-service', dir: '../order-services', command: 'npm', args: ['run', 'server'] },
  { name: 'delivery-service', dir: '../delivery-services', command: 'python', args: ['run.py'] },
];

services.forEach(service => {
  const proc = spawn(service.command, service.args, {
    cwd: path.join(__dirname, service.dir),
    stdio: 'inherit',
    shell: true
  });

  proc.on('close', (code) => {
    console.log(`${service.name} exited with code ${code}`);
  });

  console.log(`${service.name} is running`);
});

// Start the API Gateway
require('./server');