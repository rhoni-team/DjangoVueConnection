# DjangoVueConnection


## Description

This repository contains a Django-based app serving as the backend, connected with a Vue.js and Vite frontend. It is configured for both development and production environments.
The code follows the tutorial from Rhoni's blog (insert the actual link [here](#)).


## Requirements

For this project, you need to have `node` and `npm` installed on your computer. We recommend using the following versions:

- node v21.7.2
- npm v8.19.1

If you already have other versions of Node.js installed, consider using `nvm` (Node Version Manager) to manage and switch between node versions.

We also used `venv` to create the Python virtual environment, but you are free to use any other tool for managing Python dependencies.

## How to install it

### _Clone this repository_

`git clone https://github.com/rhoni-team/DjangoVueConnection`

### _Create a Python environment and install Python Dependencies_

```bash
cd DjangoVueConnection
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
### _Install Vue dependencies_

```bash
cd frontend
npm install
```

## Running in development mode

We are going to run the project in two different terminals.

In the first one, navigate to the `frontend` folder and run:

```bash
npm run dev
```

In the second terminal, navigate to the `django_vue_demo` folder and run:

```bash
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser. You should see a homepage displaying the integration of Django and Vue.js.
