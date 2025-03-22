# QuickFood - Food Delivery API

QuickFood is a robust food delivery API built with Django and Django REST Framework. It allows users to browse restaurants, view menus, place orders from multiple restaurants, and track order status. Restaurant owners can manage their restaurants, menus, and orders through a comprehensive dashboard.

## Features

### User Features
- Browse restaurants and menu items
- Place orders from multiple restaurants in a single checkout
- Track order status
- View order history

### Restaurant Owner Features
- Create and manage restaurant profile (with images)
- Add, update, and delete menu items (with images)
- Manage incoming orders
- Update order status
- Access dashboard with statistics and recent items

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register a new user
- `POST /api/users/login/` - Login and get access token

### Restaurant Management
- `POST /api/create-restaurant/` - Create a new restaurant
- `PUT /api/update-restaurant/` - Update restaurant details
- `DELETE /api/delete-restaurant/` - Delete a restaurant
- `GET /api/restaurants/` - List all restaurants
- `GET /api/restaurant/<restaurant_id>/` - Get restaurant details

### Menu Management
- `POST /api/create-menus/` - Add a menu item
- `PUT /api/menu-update/<menu_id>/` - Update a menu item
- `DELETE /api/delete-menu/<id>/` - Delete a menu item
- `GET /api/menu-items/` - List all menu items
- `GET /api/menu-item/<id>/` - Get menu item details
- `GET /api/restaurant-menu-items/` - Get all menu items for owner's restaurant

### Order Management
- `POST /api/create-order/` - Create a new order (supports multiple restaurants)
- `GET /api/my-orders/` - Get user's order history
- `POST /api/update-order-status/<id>/` - Update order status
- `GET /api/user-orders/` - Get all orders for restaurant owner


## Technical Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Media Storage**: Local storage with WhiteNoise for serving static files

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/sakayat/quickfood-backend.git
   cd quickfood-backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure database in settings.py

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```
