from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api/v1')          #Make sure you are adding the correct version

from .import posts, users
