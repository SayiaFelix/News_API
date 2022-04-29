# from flask import Blueprint

# from . import error
# main = Blueprint('main',__name__)
# from . import views


from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

from app import views