# Django - Boilerplate Project

[![Python Version](https://img.shields.io/badge/python-3.11-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-5.1-brightgreen.svg)](https://djangoproject.com)

## Django 5.1

Run your app in a Virtual Environment: http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html

Generate SECRET_KEY:
```shell
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Install the requirements:
```shell
pip install -r requirements.txt
```

Run the development server:
```shell
python manage.py runserver
```