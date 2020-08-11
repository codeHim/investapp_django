# Investapp django

This is a simple django project that stores and provides Funds investment related history data.


## Prerequisites
- python3
- venv (virtual environment)
- pip3

## How to install and run the project

- create a virtualenv `env` and activate by running `source env/bin/activate/
- `pip install -r requirements.txt` to install all dependencies in virtual env.
- `python manage.py makemigrations` & `python manage.py migrate` to create and migrate db related data to sqllite3.
- `python manage.py feed` to populate NAV history data into db tables
-`python manage.py runserver` to start the development server.

-Once the development server starts, go to the angular `investapp angular` project and run it to access `http://localhost:4200/test`
