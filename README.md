# Building a RESTful API with Flask

## Overview

This project demonstrates how to build a robust RESTful API using Flask. The API includes comprehensive error handling, JWT-based authentication, secure file uploads, and well-organized public and admin (protected) routes. By completing this project, you'll gain hands-on experience in developing scalable web services with Flask.

## Table of Contents

- Features
- Project Structure
- Installation
- Usage
- Endpoints

  
## Features

- **Error Handling:** Custom error handlers for 400, 401, 404, 500, and other HTTP status codes ensure consistent error responses.
- **Authentication:** Secure JWT-based user authentication with login endpoints and protected routes.
- **File Handling:** Validated file uploads that check file type and size, with files stored in a secure project folder.
- **Public & Admin Routes:** Clear separation between public endpoints (accessible to everyone) and protected endpoints (for authenticated users only).
- **CRUD Services:** Complete set of CRUD operations for managing items within the API.
- **Modular Architecture:** Organized project structure using Flask Blueprints for improved maintainability and scalability.

## Project Structure
```/project
├── app
│    ├── init.py         # Application factory and extension initialization
│    ├── config.py           # Configuration settings (database, JWT, file uploads, etc.)
│    ├── models.py           # SQLAlchemy models for Users and Items
│    ├── auth.py             # Authentication routes (login, token-protected routes)
│    ├── items.py            # CRUD endpoints for items (public & protected)
│    └── file_routes.py      # File upload endpoint and validation logic
├── migrations/             # Database migration scripts (if using Flask-Migrate)
├── static/                 # (Optional) Static assets for the project
├── templates/              # (Optional) HTML templates if a frontend is included
├── tests/                  # Unit and integration tests
├── requirements.txt        # List of project dependencies
├── README.md               # Project documentation (this file)
└── run.py                  # Entry point to run the Flask application
```

## Installation

1. **Clone the repository:**

  ```bash
  git clone https://github.com/yourusername/your-repo-name.git
  cd your-repo-name

2. **Create a virtual environment:**
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate


3. **Install the dependencies:**
  pip install -r requirements.txt

Configuration

Before running the project, ensure you have the proper environment variables set up or adjust the settings in the app/config.py file. Important configurations include:
	•	Database URI: Update the connection string for your MySQL (or preferred) database.
	•	JWT Secret Key: Replace the placeholder with a secure secret key.
	•	File Uploads: The UPLOAD_FOLDER is configured to securely store uploaded files.

For local development, consider creating a .env file to manage sensitive data.

# Usage

To run the application, execute the following command:
  python run.py

Once the server is running, access the API endpoints via your favorite API testing tool (e.g., Postman).

# Endpoints

## Authentication
- **Login:** `POST /login`  
  Expects a JSON payload with `"username"` and `"password"`. Returns a JWT token on successful authentication.
- **Protected Example:** `GET/POST /protected`  
  Requires a valid JWT token in the `Authorization` header.

## File Handling
- **Upload File:** `POST /upload`  
  Authenticated endpoint that accepts file uploads. Validates file type and size before storing the file.

## Items
- **Public Items:** `GET /public/items`  
  Retrieves a list of items without requiring authentication.

- **CRUD Operations:**
  - `GET /items` – List all items (requires JWT).
  - `POST /items` – Create a new item (requires JWT).
  - `GET /items/<item_id>` – Retrieve details of a specific item (requires JWT).
  - `PUT /items/<item_id>` – Update an existing item (requires JWT).
  - `DELETE /items/<item_id>` – Delete an item (requires JWT).
