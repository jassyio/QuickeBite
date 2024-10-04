# API Specifications

## User Service

### Endpoints

- **POST /register**
  - Description: Register a new user.
  - Request Body: 

    ```json
    {
      "username": "string",
      "password": "string",
      "email": "string"
    }
    ```

  - Response:

    ```json
    {
      "message": "User registered successfully"
    }
    ```

- **POST /login**
  - Description: Authenticate a user and return a JWT.
  - Request Body:

    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```

  - Response:

    ```json
    {
      "token": "jwt_token"
    }
    ```

## Restaurant Service

### Endpoints

- **GET /restaurants**
  - Description: Get a list of all restaurants.
  - Response:

    ```json
    [
      {
        "id": "string",
        "name": "string",
        "menu": "array"
      }
    ]
    ```

- **POST /restaurants**
  - Description: Add a new restaurant.
  - Request Body:

    ```json
    {
      "name": "string",
      "menu": "array"
    }
    ```

  - Response:

    ```json
    {
      "message": "Restaurant added successfully"
    }
    ```

## Order Service

### Endpoints

- **POST /orders**
  - Description: Create a new order.
  - Request Body:

    ```json
    {
      "userId": "string",
      "restaurantId": "string",
      "items": "array"
    }
    ```

  - Response:

    ```json
    {
      "orderId": "string",
      "status": "string"
    }
    ```

- **GET /orders/:orderId**
  - Description: Get the status of an order.
  - Response:

    ```json
    {
      "orderId": "string",
      "status": "string"
    }
    ```

## Delivery Service

### Endpoints

- **POST /deliveries**
  - Description: Assign a delivery to a delivery person.
  - Request Body:
    ```json
    {
      "orderId": "string",
      "deliveryPersonId": "string"
    }
    ```
  - Response:
    ```json
    {
      "message": "Delivery assigned successfully"
    }
    ```

- **GET /deliveries/:deliveryId**
  - Description: Get the status of a delivery.
  - Response:
    ```json
    {
      "deliveryId": "string",
      "status": "string"
    }
    ```

## Admin Service

### Endpoints

- **GET /admin/users**
  - Description: Get a list of all users.
  - Response:
    ```json
    [
      {
        "id": "string",
        "username": "string",
        "email": "string"
      }
    ]
    ```

- **DELETE /admin/users/:userId**
  - Description: Delete a user.
  - Response:
    ```json
    {
      "message": "User deleted successfully"
    }
    ```

- **GET /admin/restaurants**
  - Description: Get a list of all restaurants.
  - Response:
    ```json
    [
      {
        "id": "string",
        "name": "string",
        "menu": "array"
      }
    ]
    ```

- **DELETE /admin/restaurants/:restaurantId**
  - Description: Delete a restaurant.
  - Response:
    ```json
    {
      "message": "Restaurant deleted successfully"
    }
    ```

- **GET /admin/orders**
  - Description: Get a list of all orders.
  - Response:
    ```json
    [
      {
        "orderId": "string",
        "userId": "string",
        "restaurantId": "string",
        "status": "string"
      }
    ]
    ```

- **DELETE /admin/orders/:orderId**
  - Description: Delete an order.
  - Response:
    ```json
    {
      "message": "Order deleted successfully"
    }
    ```

- **GET /admin/deliveries**
  - Description: Get a list of all deliveries.
  - Response:
    ```json
    [
      {
        "deliveryId": "string",
        "orderId": "string",
        "deliveryPersonId": "string",
        "status": "string"
      }
    ]
    ```

- **DELETE /admin/deliveries/:deliveryId**
  - Description: Delete a delivery.
  - Response:

    ```json
    {
      "message": "Delivery deleted successfully"
    }
    ```

## Common Response Format

All endpoints should return responses in the following format:

```json
{
  "status": "success",
  "data": {},
  "message": "string"
}

Incase of error the return response in the following format:

```json
{
    "status": "error",
    "message": "string"
}