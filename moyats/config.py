command = '/root/venv/bin/gunicorn'
pythonpath = '/root/venv'
bind = 'unix:/root/moyats/moyats/moyats.sock'
workers = 3
accesslog='/root/moyats/logs/access.log'
raw_env = [
    "FIREBASE_KEY_PATH=/Users/mac/projects/moyat-project/moyats/moyats/moyats-60dfd-firebase-adminsdk-zvze4-7bdd04b1d7.json",
    "DJANGO_SECRET_KEY=django-insecure-0w*)t5r&shsv9b0&za50&j6!az6z2t1hdunlzj01e()(!8a26s",
    "DATABASE_NAME=moyatsdb",
    "DATABASE_USER=postgres",
    "DATABASE_PASSWORD=postgres",
    "DATABASE_HOST=127.0.0.1",
    "DATABASE_PORT=5432",
]

wsgi_app = "moyats.wsgi:application"
