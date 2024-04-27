from flask import flash, render_template, url_for, redirect
from flask_login import current_user, logout_user, login_user, login_required
from app.account import bp
from app.extensions import db, login_manager
from app.models.account import Account
from werkzeug.security import generate_password_hash, check_password_hash
from app.account.forms import LoginForm, RegistrationForm


@login_manager.user_loader
def load_user(account_id):
    return Account.query.get(int(account_id))

@bp.route('/')
def index():
    return render_template("account/index.html")



@bp.route("/login", methods=["GET", "POST"])
def login():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for("account.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Account.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for("game.index"))
            else:
                flash("Login failed, wrong password ", "danger")
        else:
            flash("Login failed, user does not exist", "danger")
    return render_template("account/login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("account.index"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for("account.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        account = Account(
            username = form.username.data,
            name = form.name.data,
            surname = form.surname.data,
            password = hashed_password,
            email = form.email.data
        )
        db.session.add(account)
        db.session.commit()
        login_user(account)
        return redirect(url_for("game.index"))
    return render_template("account/register.html", form=form)
