# Django ToDo Application

## Introduction

This is a simple ToDo application built using Django, which allows users to manage their tasks effectively. The application provides basic CRUD (Create, Read, Update, Delete) functionality, enabling users to add, edit, view, and delete tasks.

## Features

- User authentication (Login and Logout)
- Create, edit, and delete tasks
- View a list of all tasks
- Mark tasks as completed or not
- Responsive design
- Built using Django's class-based views (CBVs) for better structure and reusability


## Technology Stack

- **Backend:** Django
- **Frontend:** HTML, CSS
- **Database:** SQLite (default)
- **Version Control:** Git

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/TonyBhaskar/Django-ToDo.git
    cd Django-ToDo
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Manage users and customer data through the Django admin panel at `http://127.0.0.1:8000/admin/`.
- **Login**: Securely log in to access and manage customer details.
- **Add Task**:Use the form on the main page to add new tasks.
- **Update Task**:Click on the edit icon next to a task to update its details.
- **Delete Task**:Click on the delete icon to remove a task.
- **Mark as Completed**:Check the box next to a task to mark it as completed.
- **Logout**: Securely log out from the application.

## Contributing

We welcome contributions to enhance the functionality of this CRM system. To contribute, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
