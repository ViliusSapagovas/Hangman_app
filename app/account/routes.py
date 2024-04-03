from flask import render_template
from app.account import bp

@bp.route('/')
def index():
    return render_template('account/index.html')