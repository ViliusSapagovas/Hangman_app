from flask import render_template
from app.statistics import bp

@bp.route('/')
def index():
    return render_template('statistics/index.html')