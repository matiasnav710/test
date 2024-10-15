# Schedule Management API

This Django application provides a CRUD API for managing weekly schedules. It uses JWT for authentication and Swagger UI for documentation.

## JWT Authentication

The application uses `djangorestframework-simplejwt` for JWT-based authentication.

1. Obtain a token:
    ```bash
    POST /api/token/ 
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

    This returns the access and refresh tokens.

2. Use the access token to authenticate requests:
    ```bash
    GET /api/timeslots/
    Authorization: Bearer <access_token>
    ```

3. Refresh the token when it expires:
    ```bash
    POST /api/token/refresh/
    {
        "refresh": "your_refresh_token"
    }
    ```
