# Django Project Setup

---

# 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>

# 2. Create & Activate the virtual environment

```bash
python -m venv env
source env/bin/activate

# 3. Install dependencies

```bash
pip install -r requirements.txt

# 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (admin)

```bash
python manage.py createsuperuser

# 6. Run the development server

```bash
python manage.py runserver

---