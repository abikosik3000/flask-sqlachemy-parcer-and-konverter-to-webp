from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user

from myapp import app, db
from myapp.forms.login import LoginForm
from myapp.models.user import User


def login(app, request):
    form = LoginForm()

    if current_user.is_authenticated:
        redirect(url_for("get_cabinet"))

    if request.method == "POST" and form.validate():

        user = db.session.query(User).filter(User.email == form.email.data).first()

        if user is None:
            flash("Аккаунт не существует")
            return redirect(request.url)

        if not user.check_password(form.password.data):
            flash("Пароль не подходит")
            return redirect(request.url)

        login_user(user, False)
        flash("Вход в систему выполнен")
        return redirect(url_for("get_cabinet"))

    return render_template("login_form.html", form=form)


def register(app, request):
    form = LoginForm()

    if current_user.is_authenticated:
        redirect(url_for("get_cabinet"))

    if request.method == "POST" and form.validate():

        user_edentity = (
            db.session.query(User).filter(User.email == form.email.data).first()
        )
        if not (user_edentity is None):
            flash("Данный email уже занят")
            return redirect(request.url)

        user = User(email=form.email.data)  # , password=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user, False)
        flash("Благодарим за регистрацию")
        return redirect(url_for("get_cabinet"))

    return render_template("register_form.html", form=form)


def logout(app, request):
    logout_user()
    flash("Выход из аккаунта выполнен")
    return redirect(url_for("login"))
