from flask import Blueprint

bp = Blueprint('statistics', __name__)

from app.statistics import routes