# Vidsyra

Unlock the Intelligence Behind Every Video — Explore. Analyze. Learn. Create. Share.

## Backend setup (Windows PowerShell)

Run these commands from the directory containing `manage.py`:

```powershell
# Activate the virtual environment
.venv\Scripts\Activate.ps1

# Install Python dependencies
pip install -r requirements.txt

# Create your local environment file
Copy-Item .env.example .env

# Check the project configuration
python manage.py check

# Create migrations for the initial domain models
python manage.py makemigrations accounts videos articles generation

# Apply migrations and create an admin user
python manage.py migrate
python manage.py createsuperuser

# Start Django
python manage.py runserver
```

## Application responsibilities

- `config`: Django project configuration and root URL routing. It is the project package, not a feature app.
- `accounts`: User model and account/authentication concerns.
- `videos`: YouTube video records, transcript records, and YouTube URL parsing/integration.
- `articles`: Generated article storage, blog listing, and article detail pages.
- `generation`: AI generation job tracking, prompt orchestration, and provider integrations.

## Database

SQLite is the active database for the first implementation. Do not switch databases while the initial schema is being built. The custom `accounts.User` model is configured; keep `AUTH_USER_MODEL` in place before the first migration.

## Frontend

Django Templates are used for server-rendered pages. Tailwind CSS is built into `static/css/output.css`, which is the stylesheet path referenced by `templates/partials/head.html`.

The current YouTube URL parser validates supported URL formats only. Metadata retrieval, transcript retrieval, and AI generation will be added as separate service steps. No generated content is faked by this foundation.
