
## Deployment

To deploy this project run

```bash
  git clone <your-repo-url>
  cd <your-project-folder>
```
```bash
  python -m venv env
  source env/bin/activate
```

```bash
  pip install -r requirements.txt
```

```bash
  python manage.py makemigrations students
  python manage.py migrate students
  python manage.py migrate
```

```bash
  python manage.py createsuperuser
```

```bash
  python manage.py runserver
```
