# Small Finance and Budgeting Application

This project focuses on the creation of a finance and budgeting application using Python and Django. The application will allow users to create budgets and track their spending habits.

Help from:

- [Poetry](https://python-poetry.org/docs/)
- [Django](https://docs.djangoproject.com/en/4.2/)
- [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
- [Basic Django Setup](https://builtwithdjango.com/blog/basic-django-setup)

## Overview

This project dives into the creation of a web-based tool designed to help users manage their personal finances effectively. It provides features for tracking income, expenses, setting budgets, and generating financial reports.

## Steps followed

### 0. Installation & Setup

- Poetry project

```bash
pip install poetry

# `poetry init --no-interaction` to initialize a pre-existing project
poetry new backend --name="finance_project"
cd backend
poetry add Django pyspark
# `poetry shell` to access the environment in the terminal
```

- Django project

```bash
poetry run django-admin startproject finance_project .

# To launch the server
poetry run python manage.py runserver
```

- Django app

```bash
poetry run python manage.py startapp finance_app
```

- Django first view

```bash
touch finance_app/urls.py
```

### 1. Create database tables for models

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate --run-syncdb
```

### 2. Create forms to able the user to add data

In this Python file `finance_app/forms.py`, we will create the forms that will be used to add data to the database.

### 3. Create the login page with the Django authentication system

Do not forget to add to the `INSTALLED_APPS` in the `settings.py` file the `allauth` and `allauth.account` apps.

```python
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_EMAIL_VERIFICATION = "none"

LOGIN_REDIRECT_URL = "home"
```

### Where I got a bit stuck / Interesting points

- To link correctly the pages, I had to add the `finance_app` to the `INSTALLED_APPS` in the `settings.py` file.
- For the templates, I had to add the `finance_app/templates` folder to the `DIRS` in the `TEMPLATES` in the `settings.py` file.
- Be careful with the `urls.py` files. There is one in the project folder and one in the app folder. The one in the project folder is the main one, and the one in the app folder is the one that will be used to link the pages of the app.
- Concerning the add of data, Django has the `ModelForm` class that allows us to create forms from models. The class `Meta` is used to specify the model and the fields that we want to use in the form (see more [here](https://docs.djangoproject.com/en/4.2/topics/db/models/#meta-options)).
- Struggling some hours with Registration and Login. I had to look carefully at the use of `UserCreationForm` and `AuthentificationForm` (see more [here](https://docs.djangoproject.com/fr/4.2/topics/auth/default/)).

### Extra: Setup of pre-commit

```bash
pip install pre-commit
```

Once the `.pre-commit-config.yaml` completed, we need to set up the git hooks scripts.

```bash
pre-commit install
```
