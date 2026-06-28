# Movie Quote API

A REST API for movie and series quotes, built with Django and Django REST Framework.

## Tech Stack
- Django
- Django REST Framework
- Jazzmin (Admin Panel)
- SQLite

## Run Locally

1. Clone the repository:
```bash
git clone https://github.com/SinaKoulani/movie-quote.git


Activate virtual environment:
powershell
.\venv\Scripts\Activate.ps1
Install dependencies:
bash
pip install django django-jazzmin python-dotenv djangorestframework
Run migrations:
bash
python manage.py migrate
Run server:
bash
python manage.py runserver