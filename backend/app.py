import os
from envyaml import EnvYAML
from flask import Flask
from config import getDBConnection
from config.constants import Constants

app = Flask(__name__)

# Load the .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(".env"))

# Read the current environment
current_env = os.getenv("FLASK_ENV", Constants.DEV_ENV)

# read file config.yaml and parse config
config_data = EnvYAML('config.yaml')

# Access configuration values for the current environment
config_for_current_env = config_data.get(current_env, {})

# Get DB Connection
conn = getDBConnection(config_for_current_env["DB"])

# Set Flask app configuration values
app.config['DEBUG'] = config_for_current_env.get("DEBUG")
app.config['PORT'] = config_for_current_env.get("PORT")

# Import all the controllers (routes)
from controller import *

@app.route("/")
def welcome():
    return "Welcome!!!"

if __name__ == "__main__":
    app.run()
