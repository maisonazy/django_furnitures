

A modern furniture website built with **Python and Django**, designed to showcase furniture products through a user-friendly web interface. The project demonstrates the development and deployment of a Django web application, with a live version hosted on Vercel.

## Live Demo

Visit the website here:

[Django Furnitures — Live Website](https://django-furnitures-q7qe.vercel.app/)

##  Project Overview

Django Furnitures is a web development project focused on presenting furniture products online. It provides a foundation for building a furniture store where customers can explore furniture and discover products for their homes and offices.

The application uses Django for backend development and HTML, CSS, and JavaScript for the website's user interface.

The project also demonstrates how a Django application can be deployed to a cloud hosting platform and made accessible online.

##  Features

The website's features depend on the functionality implemented in the project.

- **Furniture Showcase:** Present furniture products through a dedicated website.
- **Product Presentation:** Display furniture images and relevant product information.
- **User-Friendly Interface:** Organize website content to make navigation easier.
- **Web-Based Access:** Allow visitors to access the website through a web browser.
- **Django Backend:** Use Django to handle server-side functionality.
- **Responsive Design:** Support different screen sizes if responsive styling has been implemented.
- **Online Deployment:** Make the website accessible through a public Vercel URL.



## Technologies Used

| Technology | Purpose |

| Python | Backend programming language |
| Django | Web application framework |
| HTML5 | Website structure |
| CSS3 | Website styling and layout |
| JavaScript | Client-side interactivity |
| SQLite or PostgreSQL | Database, depending on project configuration |
| Git | Version control |
| GitHub | Source code hosting |
| Vercel | Website deployment |


### Prerequisites

Make sure you have installed:

- Python
- pip
- Git
- A code editor, such as Visual Studio Code

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/maisonazy/django_furnitures.git
```

Navigate into the project directory:

```bash
cd django_furnitures
```

**Important:** Ensure that `django_furnitures` is the correct repository name and that the repository is public or you have permission to access it.

### 2. Create a Virtual Environment

On Linux or Ubuntu, run:

```bash
python3 -m venv env
```

Activate the environment:

```bash
source env/bin/activate
```

### 3. Install Dependencies

If your project contains a `requirements.txt` file, install its dependencies:

```bash
pip install -r requirements.txt
```

If the file does not exist, install Django in your virtual environment:

```bash
pip install django
```

Install any other dependencies required by your project.

### 4. Configure Environment Variables

If your application uses environment variables, configure them before running the project.

For example, production settings may include:

- `SECRET_KEY`
- `DEBUG`
- `DATABASE_URL`
- `ALLOWED_HOSTS`

Use the variable names expected by your Django settings.

**Security:** Never commit production secret keys, database passwords, or other credentials to GitHub.

### 5. Apply Database Migrations

Run:

```bash
python manage.py migrate
```

This creates the database tables required by your Django application.

### 6. Create an Administrator Account

If your project uses Django's administration interface, run:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 7. Start the Development Server

Run:

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

You should now be able to access the locally running website.

## Django Administration

Django provides an administration interface for managing application data when the appropriate models and admin registrations have been configured.

To access it locally, visit:

http://127.0.0.1:8000/admin/

Log in using the administrator account you created.

Depending on the functionality implemented in this project, the admin interface can be configured to manage furniture products, categories, images, and other application data.

