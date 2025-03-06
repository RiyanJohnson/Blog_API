# Getting Started

### Create a python environment and activate
'python -m venv env'
'env\Scripts\activate'

### Clone the repository to the direcrory of the env
'git clone https://github.com/RiyanJohnson/Blog_API'

### Install the Django-Rest-Framework pacakge
'pip install djangorestframework'

### Make migrations
'python manage.py makemigrations'
'python manage.py migrate'

### Run the server
'python manage.py runserver'

# Blog App API Documentation

Welcome to the Blog App API documentation. This RESTful API allows users to register, authenticate, create posts, comment on posts, and manage their content. The API uses token-based authentication to secure endpoints.

## Base URL

All API endpoints are prefixed with the base URL:

'''
http://127.0.0.1:8000/
'''

## Authentication

This API uses token-based authentication. After logging in, users receive a token, which must be included in the `Authorization` header of subsequent requests.

**Header Format:**

'''
Authorization: Token <your_token>
'''

## Endpoints

### 1. User Registration

**Endpoint:** `/api/register/`

**Method:** `POST`

**Description:** Registers a new user with a username, email address, and password.

**Request Parameters:**

- `username` (string): The user's chosen username.
- `email` (string): The user's email address.
- `password` (string): The user's password.

**Response:**

- `201 Created`: User registered successfully.
- `400 Bad Request`: Invalid input data.

### 2. User Login

**Endpoint:** `/api/login/`

**Method:** `POST`

**Description:** Authentates a user and returns an authentication token.

**Request Parameters:**

- `username` (string): The user's username.
- `password` (string): The user's password.

**Response:**

- `200 OK`: Returns the authentication token.
- `400 Bad Request`: Invalid credentials.

### 3. User Logout

**Endpoint:** `/api/logout/`

**Method:** `POST`

**Description:** Logs out the authenticated user by deleting their token.

**Headers:**

- `Authorization: Token <your_token>`

**Response:**

- `204 No Content`: User logged out successfully.
- `401 Unauthorized`: Authentication token is missing or invalid.

### 4. View All Posts

**Endpoint:** `/api/posts/`

**Method:** `GET`

**Description:** Retrieves a list of all posts.

**Response:**

- `200 OK`: Returns a list of posts.

### 5. Create a Post

**Endpoint:** `/api/create/`

**Method:** `POST`

**Description:** Creates a new post.

**Headers:**

- `Authorization: Token <your_token>`

**Request Parameters:**

- `title` (string): The title of the post.
- `content` (string): The content of the post.

**Response:**

- `201 Created`: Post created successfully.
- `400 Bad Request`: Invalid input data.
- `401 Unauthorized`: Authentication token is missing or invalid.

### 6. View a Specific Post

**Endpoint:** `/api/posts/<post_id>/`

**Method:** `GET`

**Description:** Retrieves details of a specific post by its ID.

**Response:**

- `200 OK`: Returns the post details.
- `404 Not Found`: Post not found.

### 7. Delete a Post

**Endpoint:** `/api/posts/<post_id>/delete/`

**Method:** `DELETE`

**Description:** Deletes a specific post by its ID. Only the author can delete their post.

**Headers:**

- `Authorization: Token <your_token>`

**Response:**

- `204 No Content`: Post deleted successfully.
- `404 Not Found`: Post not found.
- `401 Unauthorized`: Authentication token is missing or invalid.

### 8. Comment on a Post

**Endpoint:** `/api/posts/<post_id>/comment/`

**Method:** `POST`

**Description:** Adds a comment to a specific post.

**Headers:**

- `Authorization: Token <your_token>`

**Request Parameters:**

- `content` (string): The content of the comment.

**Response:**

- `201 Created`: Comment added successfully.
- `404 Not Found`: Post not found.
- `401 Unauthorized`: Authentication token is missing or invalid.

## Admin Page

The admin interface is accessible at:

'''
http://127.0.0.1:8000/admin/
'''

Authorized staff members can manage users, posts, and comments through this interface.

## Notes

- Ensure that the `Authorization` header is included in all requests that require authentication.
- Replace `<your_token>` with the token obtained after logging in.
- Replace `<post_id>` with the ID of the specific post you want to interact with.

For more details on implementing token-based authentication in Django REST Framework, refer to the following resources:

- [How to Implement Token Authentication using Django REST Framework](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html)

