# DjangoVueConnection


## Description

This repository contains a Django-based app serving as the backend, connected with a Vue.js and Vite frontend. It is configured for both development and production environments.
The code follows the series of tutorials from [Rhoni's blog](https://rhonidev.com/blog/) about how to connect Django with VueJS and ViteJS:

- [Connecting Django and Vue for development](https://rhonidev.com/blog/connecting-django-and-vue-for-development)

And coming soon...
- Deploying Django and Vue for Production
- Two-Way Communication: Managing Requests and Responses between VueJs and Django


## Requirements

For this project, you need to have `node` and `npm` installed on your computer. We recommend using the following versions:

- node 22.17.1
- npm 10.9.2

If you already have other versions of Node.js installed, consider using `nvm` (Node Version Manager) to manage and switch between node versions.

We also used `venv` to create the Python virtual environment, but you are free to use any other tool for managing Python dependencies.


### How to use this repository

This repository include all the code that can be obtained after following the complete series of tutorials about how to connect Django and Vue in Rhoni's blog.

You have several options:

1) Clone the [complete repository](#getting-the-complete-django---vue-application)

You will get a functional app for both modes, development and production. Data between Django and Vue is exchanged by using Axios.

2) Clone [only part of it to follow a specific tutorial](#getting-partial-code-of-django---vue-application):

- Django and Vue connected in development mode.

- Django and Vue connected in production mode.

___


# Getting the complete Django - Vue application


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
cd demo
cd frontend
npm install
```

## Running in development mode

Ensure the `DEBUG` variable is set to `True` in the `settings.py` file, if it hasn't been set already.

```bash
DEBUG = True
```

Now we will start the project by running it in two different terminals.

In the first one, navigate to the `frontend` folder and run:

```bash
npm run dev
```

In the second terminal, with your Python environment activated, navigate to the `demo` folder and run:

```bash
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser. You should see a homepage displaying the integration of Django and Vue.js in development mode.

## Running in production mode

Ensure the `DEBUG` variable is set to `False` in the `settings.py` file, if it hasn't been set already.

```bash
DEBUG = False
```

In the terminal, navigate to the `frontend` folder and run:

```bash
npm run build
```

Now navigate to the folder `demo` and run:

```bash
python manage.py collectstatic
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser. You should see a homepage displaying the integration of Django and Vue.js in production mode.



# Getting partial code of the Django-Vue application

## How to install it

### _Clone a brach_

To install the code for the **[Connecting Django and Vue for development](https://rhonidev.com/blog/connecting-django-and-vue-for-development)** tutorial, clone the branch `django_vue_for_development`.

```bash
git clone git@github.com:rhoni-team/DjangoVueConnection.git --branch django_vue_for_development --single-branch
```

Or to install the code for the **"Deploying Django and VueJs with Vite for Production"** tutorial (coming soon) clone the `django_vue_for_production` branch.

```bash
git clone git@github.com:rhoni-team/DjangoVueConnection.gi --branch django_vue_for_production --single-branch
```

### _Install necessary dependencies_

After cloning the project, you will need to install the necessary dependencies for Python and Vue:

1. [Create a Python environment and install Python Dependencies](#create-a-python-environment-and-install-python-dependencies)

2. [Install Vue dependencies](#install-vue-dependencies)


## How to run it

Both branches can be started on development mode. To do this, follow the steps outlined in the [Running in development mode](#running-in-development-mode) section.

The `django_vue_for_production` branch is also set up for production. To run it in production mode, follow the steps from the [Running in production mode](#running-in-production-mode) section.
