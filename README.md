# Movie Quote App

A full-stack movie and series quote application built with **Django** for the backend and **Vue.js** for the frontend.

## Project Structure
```bash
movie-quote/
├── frontend/       # Vue.js frontend
├── manage.py       # Django entry point
├── venv/           # Virtual environment (not tracked)
├── .env            # Environment variables (not tracked)
└── ...
Tech Stack
Backend
Django
Django REST Framework
Jazzmin
SQLite
Frontend
Vue.js
Vite
JavaScript
Run Locally
1) Clone the repository
bash
git clone https://github.com/SinaKoulani/movie-quote.git
cd movie-quote
2) Backend setup
Create and activate virtual environment:

powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
Install backend dependencies:

powershell
pip install django django-jazzmin python-dotenv djangorestframework
Run backend server:

powershell
cd movie-quote
cd backend
python manage.py migrate
python manage.py runserver
3) Frontend setup
Go to frontend folder:

powershell
cd frontend
Install dependencies:

powershell
npm install
Run development server:

powershell
npm run dev
Notes
Make sure Python and Node.js are installed.
venv/, .env, node_modules/, and generated files are excluded from Git.
