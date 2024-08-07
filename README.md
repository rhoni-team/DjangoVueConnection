# DjangoVueConnection


## Description

This repository contains a Django-based app serving as the backend, connected with a Vue.js and Vite frontend. It is configured for both development and production environments.
The code follows the series of tutorials from Rhoni's blog about how to connect Django with VueJS and ViteJS (insert the actual link [here](#)):

- How to connect Django with VueJs and Vite for development
- How to connect Django, VueJs, and Vite for production
- How to send requests from VueJs and handle them in the Django backend, as well as sending responses back to the frontend


## Requirements

For this project, you need to have `node` and `npm` installed on your computer. We recommend using the following versions:

- node v21.7.2
- npm > 7

If you already have other versions of Node.js installed, consider using `nvm` (Node Version Manager) to manage and switch between node versions.

We also used `venv` to create the Python virtual environment, but you are free to use any other tool for managing Python dependencies.


### How to use this repository

This repository include all the code that can be obtained after following the complete series of tutorials about how to connect Django and Vue in Rhoni's blog.

You have several options:

1) Clone the [complete repository](#getting-the-complete-django---vue-application)

You will get a functional app for both modes, development and production. Data between Django and Vue is requested by using Axios.

2) Clone a release to follow a specific tutorial:

- Release 1.0 - Django and Vue connected in development mode.

- Release 2.0 - Django and Vue connected in production mode.

- Release 3.0 - Django and Vue connected with Axios

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

We are going to run the project in two different terminals.

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

In the Django's `settings.py` file set DEBUG variable to False:

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