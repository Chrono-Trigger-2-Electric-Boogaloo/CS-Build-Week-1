release: python manage.py migrate
web: gunicorn adv_project.wsgi:application --workers=3 --log-file -