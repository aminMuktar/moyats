command = '/home/alpha/Documents/Projects/venv/bin/gunicorn'
pythonpath = '/home/alpha/Documents/Projects/venv'
bind = 'unix:/home/alpha/Documents/Projects/moyats/moyats/moyats.sock'
workers = 3
accesslog='/home/alpha/Documents/Projects/moyats/logs/access.log'
raw_env = [
    "FIREBASE_KEY_PATH=/home/alpha/Documents/Projects/moyats/moyats/moyats-60dfd-firebase-adminsdk-zvze4-7bdd04b1d7.json",
    "DJANGO_SECRET_KEY=django-insecure-0w*)t5r&shsv9b0&za50&j6!az6z2t1hdunlzj01e()(!8a26s",
    "DATABASE_NAME=moyatsdb",
    "DATABASE_USER=postgres",
    "DATABASE_PASSWORD=root",
    "DATABASE_HOST=127.0.0.1",
    "DATABASE_PORT=5432",
]

wsgi_app = "moyats.wsgi:application"
