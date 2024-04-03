from flask import render_template
from app.account import bp
from app.extensions import db
from app.models.account import Account

@bp.route('/')
def index():
    return render_template('account/index.html')