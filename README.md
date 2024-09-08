# DRF-Book-Project

This is a Django-based API project that provides functionalities related to books, including creating, retrieving, updating, and deleting book records. The project is set up using Django and Django REST Framework.

## Features

- Manage authors, categories, and books.
- CRUD operations for authors, categories, and book records.
- SQLite database for local development.

## Project Structure

- **config/**: Django project configuration files.
- **books/**: Application containing models, views, serializers, URLs, and migrations for managing books.
- **manage.py**: Command-line utility for administrative tasks.
- **requirements.txt**: List of dependencies required for the project.

## Setup Instructions

### Prerequisites

- Python 3.8 or later
- Django 3.2 or later
- Django REST Framework

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mirmakhmudoff/DRF-Book-Project
    cd DRF-Book-Project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000/`. Use an API client like Postman or curl to interact with the endpoints.

### Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage books and categories.

## API Endpoints

### Authors

- **GET /authors/**: Retrieve a list of all authors.
- **POST /authors/**: Create a new author.
- **GET /authors/{id}/**: Retrieve details of a specific author.
- **PUT /authors/{id}/**: Update a specific author.
- **DELETE /authors/{id}/**: Delete a specific author.

### Categories

- **GET /categories/**: Retrieve a list of all categories.
- **POST /categories/**: Create a new category.
- **GET /categories/{id}/**: Retrieve details of a specific category.
- **PUT /categories/{id}/**: Update a specific category.
- **DELETE /categories/{id}/**: Delete a specific category.

- ### Books

- **GET /books/**: Retrieve a list of all books.
- **POST /books/**: Create a new book.
- **GET /books/{id}/**: Retrieve details of a specific book.
- **PUT /books/{id}/**: Update a specific book.
- **DELETE /books/{id}/**: Delete a specific book.
