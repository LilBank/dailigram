![Alt text](diary/static/pictures/logo.png)

[![Build Status](https://travis-ci.com/bankkeez/dailigram.svg?branch=master)](https://travis-ci.com/bankkeez/dailigram)

[![codecov](https://codecov.io/gh/bankkeez/dailigram/branch/master/graph/badge.svg)](https://codecov.io/gh/bankkeez/dailigram)

**Dailigram** is an online diary which provides users free space to instantly preserve their moments and memories, including pictures, and share them online to exchange user’s life stories. Plus, it's accessible anywhere and anytime through the internet, which is surely more convenient than carrying a diary book.
Our target group is a typical internet users who prefer writing journal online. 

## Team Members

ID           |           Name           |               Roles
-------------|--------------------------|-------------------------------------
6010545854   |   Piyawat Setthitikun    |       Scrum Master, Developer
6010545897   |   Vichaphol Thamsuthikul |              Developer
6010546630   |   Kittin Vatabutr        |              Developer

## Documents

- Iteration Plan - [Google Docs](https://docs.google.com/document/d/1y1627RIie1AMI3jERJbZHnNt9rR0pr2baXCQTu89Q1I/edit?usp=sharing)
- Task Board - [Trello](https://trello.com/b/F2yv7lWS/dailigram-project)  
- Issue Tracker - [Github issues](https://github.com/bankkeez/dailigram/issues)

## Prerequisite

You must download the following to be able to run.

- `Python`  [download](https://www.python.org/downloads/)
- `Heroku`  [download](https://devcenter.heroku.com/articles/heroku-cli)
- `Node.js` [download](https://nodejs.org/en/download/package-manager/)
- `.env`  **Please ask project owner privately for the environment variables.**

## Installation Steps

**Step 1: Open the terminal and clone the project to your local directory.**

    ```
    git clone https://github.com/bankkeez/dailigram.git
    ```

**Step 2: Go to the directory.**

    ```
    cd dailigram/ 
    ```

**Step 3: Activate a virtualenv.**

    For Mac and Linux:

    ```
    source .venv/bin/activate
    ```

    For Windows:

    ```
    .venv/bin/activate
    ```

**Step 4: Install the dependencies.**

    ```
    (venv) pip install -r requirements.txt
    ```

**Step 5: Run Application Locally.**

    Run the project server by typing the following command.

    ***For Mac:***

    ```
    (venv) heroku local web
    ```

    ***For Windows:***

    You have to create file name `Procfile.windows` in your root directory and write this  
    `web: python manage.py runserver localhost:8000` then you are ready to run.

    ```
    (venv) heroku local web -f Procfile.windows
    ```

**Step 6: Leave the virtualenv.**

    When done, you have to leave your virtualenv, you can simply run:

    ```
    (venv) deactivate
    ```