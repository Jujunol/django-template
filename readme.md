# Django Template

## Brief

The aim of this project is to take off a lot of the initial building of a react app with django and materialize.

This Django Template comes prepackaged with:
- Django
- Materialize-Css
- Webpack
- React
- Scss transpiliation system
- Jinja2 templating system

Additionally, there is also:
- A modified env system to change settings based on your environment
- The ability to read from an .env file (refer to .env.example)
- Useful common css helpers built on-top of materialize

## Variations
We keep different variations/prepackages on different branches

- [API](https://github.com/Jujunol/django-template/tree/api) comes with a backend API system for working with JSON. Please note that does not contain a token auth system. 


## Installation (Linux & Mac)

### Downloading a clone of the repo
1. `git clone https://github.com/Jujunol/django-template`
1. `cd django-template`
1. `rm -rf .git && git init` (or for powershell `rm -r -force .git ; git init`)
1. `cp .env.example .env`

### Setting up the virtualenv (optional but recommended)
1. `python -m virtualenv env`
1. `env/bin/activate`

### Setting up Django
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. `python manage.py runserver`

### Setting up NPM + Webpack
1. `npm i`
1. `npm start` this will start our webpack and livereload servers


## Testing our setup
Open your browser and go to `http://localhost:8000`