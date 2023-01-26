# OpenAI API - Python app

This is an app to get the US president's name generator using the OpenAI API. The main purpose in building this app was to try out the OpenAI's API.

Referneces: [quickstart tutorial](https://beta.openai.com/docs/quickstart). Check out the tutorial.

It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. 

Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd my-openai-app-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! 

This app is created on the basis of this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
