# Blog Posting Website
**Welcome to Xomar Website project built using the Django framework. This ReadMe file will guide you through the setup, structure, and functionality of the project.**

### Table of Contents
1. Introduction
2. Features
3. Technologies Used
4. Installation
5. Usage
6. Project Structure
7. Contributing

### Introduction
This project is a simple blogging website where users can create, edit, and delete blog posts. It is built using the Django framework, which follows the Model-View-Template (MVT) architectural pattern.

### Features
- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts
- Categorize posts with specific author
- Pagination

### Technologies Used
- Django
- SQLite 
- HTML, CSS
- Bootstrap (for styling)

### Installation
**Prerequisites**
- Python 3.12.1
- Pip (Python package installer)
- Virtualenv (recommended)

**Steps**
1. Clone the repository
```
git clone https://github.com/BirtukanK/Blog_site.git
cd Blog_site
```
2. Create and activate a virtual environment
```
python -m venv venv
./venv/Scripts/activate (in windows)
```
3. Install the required packages
```
pip install -r requirements.txt
```
4. Apply migrations
```
python manage.py migrate
```
5. Create a superuser
```
python manage.py createsuperuser
```
6. Run the development server
```
python manage.py runserver
```
7. Access the website
Open your web browser and go to `http://127.0.0.1:8000`

### Usage
1. User Registration and Authentication

- Navigate to the registration page to create a new account.
- Use your credentials to log in.

2. Creating a Blog Post

- After logging in, navigate to the "New Post" page.
- Fill out the form and submit to create a new blog post.

3. Managing Blog Posts
- Edit or delete your own posts from the post detail page.

4. Pagination
- Navigate through multiple pages of posts using pagination links.

### Author
- Birtukan Kuma
- birtukanKuma1113@gmail.com

<!-- ### Project Structure
Blog_site/
|blog_site
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── blog/
│   │       ├── about.html
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       ├── user_posts.html
│   └── static/
│       └── blog/
│           ├── css/
├── blog_site/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── profile.html
│   │       ├── profile.html
│   │       ├── register.html
├── manage.py
└── requirements.txt -->
