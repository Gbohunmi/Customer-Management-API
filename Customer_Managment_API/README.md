# Customer Management API

This is a Django REST Framework project providing a simple API for managing customers and their associated orders. It features custom user authentication using email and JWT (JSON Web Tokens).

## Features

*   **Customer Management:** Full CRUD (Create, Read, Update, Delete) operations for customer records (name, email, phone, address).
*   **Order Management:** Full CRUD operations for orders associated with customers (order date, status, total).
*   **Custom User Model:** Uses email as the primary identifier for login instead of username.
*   **JWT Authentication:** Secure API endpoints using `rest_framework_simplejwt` for token-based authentication (access and refresh tokens).
*   **Filtering, Searching, and Ordering:** API endpoints for listing customers and orders support:
    *   Filtering by specific fields (e.g., `?name=...`, `?status=...`).
    *   Searching across multiple fields (e.g., `?search=...`).
    *   Ordering results (e.g., `?ordering=name`, `?ordering=-created_at`).
*   **Permissions:** API endpoints require users to be authenticated.

## Technologies Used

*   Python
*   Django
*   Django REST Framework (DRF)
*   Simple JWT (for JWT Authentication)
*   Django Filter (for filtering capabilities)
*   SQLite (default database)

## Project Structure


Customer-Management-API/
├── Customer_Managment_API/ # Django Project Directory
│ ├── api/ # Django App for the API
│ │ ├── migrations/
│ │ ├── init.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── models.py # Defines CustomUser, Customer, Order models
│ │ ├── serializers.py # Defines DRF serializers
│ │ ├── tests.py
│ │ ├── urls.py # API specific URLs (customers, orders, token auth)
│ │ └── views.py # API viewsets (Customer, Order)
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py # Project settings (apps, db, auth, jwt config)
│ ├── urls.py # Main project URLs (admin, api/)
│ └── wsgi.py
├── manage.py # Django management script
└── db.sqlite3 # Default database file
└── README.md # This file
└── requirements.txt # Project dependencies (You need to create this)



## Prerequisites

- Python 3.10 or later
- pip (Python package installer)
- Virtual environment tool (optional, but recommended)

## Setup and Installation

Follow these steps to set up the project on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd Customer-Management-API
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    If a requirements.txt file exists run

    ```bash
    pip install -r requirements.txt
    ```
    ```
    # requirements.txt
    Django>=5.0 # Adjust version as needed
    djangorestframework
    djangorestframework-simplejwt
    django-filter
    ```

    Otherwise install the essential packages manually:
    ```bash
    pip install django djangorestframework djangorestframework-simplejwt django-filter
    ```    


4.  **Apply Database Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser:**
    This user is needed to log in and obtain JWT tokens initially.
    ```bash
    python manage.py createsuperuser
    ```
    You will be prompted to enter an email address (use this for login), and a password.

6.  **Create a User:**
    This user is needed to log in and obtain JWT tokens initially.
    ```bash
    python manage.py create_user
    ```
    You will be prompted to enter an email address (use this for login), and a password.

## Running the Project

1.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```
2.  The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

All endpoints under `/api/` except for token endpoints require authentication using a JWT Bearer Token in the `Authorization` header.

**Base URL:** `http://127.0.0.1:8000/api/`

### Authentication

*   **Obtain Tokens:**
    *   `POST /api/token/`
    *   **Request Body:** `{ "email": "user@example.com", "password": "yourpassword" }`
    *   **Response:** `{ "refresh": "...", "access": "..." }`
*   **Refresh Access Token:**
    *   `POST /api/token/refresh/`
    *   **Request Body:** `{ "refresh": "<refresh_token>" }`
    *   **Response:** `{ "access": "<new_access_token>" }`

### Customers

*   **Endpoint:** `/api/customers/`
*   **Methods:**
    *   `GET`: List all customers.
        *   *Filtering:* `?name=...`, `?email=...`
        *   *Searching:* `?search=...` (searches `name`, `email`, `address`, `phone_number`)
        *   *Ordering:* `?ordering=name`, `?ordering=-created_at` (prefix with `-` for descending)
    *   `POST`: Create a new customer.
        *   **Request Body:** `{ "name": "...", "email": "...", "phone_number": ..., "address": "..." }` (email and address are optional based on model)
*   **Endpoint:** `/api/customers/{id}/`
*   **Methods:**
    *   `GET`: Retrieve a specific customer.
    *   `PUT`: Update a specific customer (requires all fields).
    *   `PATCH`: Partially update a specific customer.
    *   `DELETE`: Delete a specific customer.

### Orders

*   **Endpoint:** `/api/orders/`
*   **Methods:**
    *   `GET`: List all orders.
        *   *Filtering:* `?customer=...` (use customer ID), `?order_date=...`, `?status=paid|unpaid`, `?total=...`
        *   *Searching:* `?search=...` (searches customer relation - likely by customer ID or name depending on DRF setup)
        *   *Ordering:* `?ordering=customer`, `?ordering=status`, `?ordering=-total`
    *   `POST`: Create a new order.
        *   **Request Body:** `{ "customer": <customer_id>, "status": "paid|unpaid", "total": "..." }`
*   **Endpoint:** `/api/orders/{id}/`
*   **Methods:**
    *   `GET`: Retrieve a specific order.
    *   `PUT`: Update a specific order (requires all fields).
    *   `PATCH`: Partially update a specific order.
    *   `DELETE`: Delete a specific order.

## Authentication Flow

1.  Send a `POST` request to `/api/token/` with your registered user's `email` and `password`.
2.  Receive `access` and `refresh` tokens in the response.
3.  For all subsequent requests to protected endpoints (like `/api/customers/` or `/api/orders/`), include the `access` token in the `Authorization` header:
    ```
    Authorization: Bearer <your_access_token>
    ```
4.  The access token has a limited lifetime (default 30 minutes in `settings.py`). If it expires, use the `refresh` token with the `/api/token/refresh/` endpoint to get a new access token.