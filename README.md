<!-- ![Alt text](diary/static/pictures/logo.png) -->
<a href="https://dailigram.herokuapp.com/"><img src="diary/static/pictures/logo.png"></a>

[![Build Status](https://travis-ci.com/bankkeez/dailigram.svg?branch=master)](https://travis-ci.com/bankkeez/dailigram)

[![codecov](https://codecov.io/gh/bankkeez/dailigram/branch/master/graph/badge.svg)](https://codecov.io/gh/bankkeez/dailigram)

**Dailigram** is an online diary which provides users free space to instantly preserve their moments and memories, including pictures. Plus, it's accessible anywhere and anytime through the internet, which is surely more convenient than carrying a diary book.
Our target group is a typical internet users who prefer writing journal online. 

## Team Members

GitHub       |           Name           |               Roles
-------------|--------------------------|-------------------------------------
bankeez      |   Piyawat Setthitikun    |       Scrum Master, Developer
kimvcp       |   Vichaphol Thamsuthikul |              Developer
Kittinske15  |   Kittin Vatabutr        |              Developer

## Documents

- Iteration Plan - [Google Docs](https://docs.google.com/document/d/1y1627RIie1AMI3jERJbZHnNt9rR0pr2baXCQTu89Q1I/edit?usp=sharing)
- Task Board - [Trello](https://trello.com/b/F2yv7lWS/dailigram-project)  
- Issue Tracker - [Github issues](https://github.com/bankkeez/dailigram/issues)

## Prerequisite

You must download the following to be able to run.

- `Python (ver.3.5 or newer)` [download site](https://www.python.org/downloads/)
- `Heroku CLI` [download site](https://devcenter.heroku.com/articles/heroku-cli)
- `Node.js` [download site](https://nodejs.org/en/download/package-manager/)
- `local environment variable` **Please ask project owner privately for the environment variables.**

## Installation Steps

### Step 1: Clone the project to your local directory.

Open the Terminal and type the following command:

    git clone https://github.com/bankkeez/dailigram.git

### Step 2: Go to the directory.

    cd dailigram/

### Step 3: Create a virtualenv.

Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.

    virtualenv venv

### Step 4: Activate the virtualenv.

Activate it before you start installing packages.

***On MacOS and Linux:***

    source venv/bin/activate

***On Windows:***

    venv\Scripts\activate

### Step 5: Install the dependencies.

Be sure that everything is installed and run in the virtualenv.

    (venv) pip install -r requirements.txt

### Step 6: Exit the virtualenv.

When done, you have to exit your virtualenv, simply type:

    (venv) deactivate

## Run Application Locally.

Activate the virtualenv before running.

***On MacOS and Linux:***

    (venv) heroku local web

***On Windows:***

You have to create file name `Procfile.windows` in your root directory and write this  
`web: python manage.py runserver localhost:5000` then you are ready to run.
    
    (venv) heroku local web -f Procfile.windows

