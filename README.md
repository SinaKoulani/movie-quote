# Movie Quote App

A full-stack movie and series quote application built with **Django** for the backend and **Vue.js** for the frontend.

## Project Structure
```bash
movie-quote/
├── backend/        # Django backend (contains manage.py)
├── frontend/       # Vue.js frontend
└── README.md
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
Navigate to the backend directory:

powershell
cd backend
Create and activate virtual environment:

powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
Install dependencies:

powershell
pip install django django-jazzmin python-dotenv djangorestframework
Run migrations and server:

powershell
python manage.py migrate
python manage.py runserver
3) Frontend setup
Open a new terminal window in the project root, then:

powershell
cd frontend
npm install
npm run dev
Notes
Make sure Python and Node.js are installed.
venv/, .env, node_modules/, and generated files are excluded from Git.
