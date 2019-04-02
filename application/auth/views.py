from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.reviews.models import Review
from application.auth.forms import LoginForm, RegisterForm, UserEditForm
from sqlalchemy.sql import text

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjänimi tai salasana väärin")


    login_user(user)
    return redirect(url_for("index"))    
    
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 
    
@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = RegisterForm())

@app.route("/auth/<user_id>/")
def auth_profile(user_id):
    stmt = text("SELECT User.id, User.username, COUNT(Review.id) AS review_count FROM User LEFT JOIN Review ON User.id = Review.user_id WHERE User.id = {} GROUP BY User.id".format(user_id))
    res = db.engine.execute(stmt)
    users = []
    for row in res:
        users.append({"id":row[1], "username":row[1], "review_count":row[2]})
    return render_template("auth/profile.html", users = users, reviews = Review.query.filter_by(user_id=user_id))

@app.route("/auth/<user_id>/", methods=["POST"])
@login_required
def auth_edit(user_id):
    user = User.query.get(user_id)
    
    form = UserEditForm()
    form.oldUsername.data = user.username
    form.username.data = user.username
    form.password.data = user.password
    form.passwordSec.data = user.password
    return render_template("auth/edit.html", form = form, user = user) 


   
@app.route("/auth/", methods=["POST"])
def auth_registerOrUpdate():
    if('create' in request.form):
        form = RegisterForm(request.form)

        if not form.validate():
            return render_template("auth/new.html", form = form)
        username = form.username.data    
        password = form.password.data
        user = User(username, password, False)
        db.session().add(user)
        db.session().commit()  
    
        login_user(user)
        
        
        
    elif('edit' in request.form):
        form = UserEditForm(request.form)

        if not form.validate():
            return render_template("auth/edit.html", form = form)
            
        oldUsername = form.oldUsername.data
        user = User.query.filter_by(username=oldUsername).first()
        
        user.username = form.username.data
        user.password = form.password.data

        db.session().commit()
        
        
        
        
    return redirect(url_for("games_index"))