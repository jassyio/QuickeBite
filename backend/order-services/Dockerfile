FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV MONGODB_URI=mongodb://mongo-db/order_db
ENV RABBITMQ_URL=amqp://rabbitmq

ENV PORT=4000

CMD ["npm", "start"]
