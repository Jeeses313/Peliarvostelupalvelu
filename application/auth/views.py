from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.reviews.models import Review
from application.likes.models import Like
from application.auth.forms import LoginForm, RegisterForm, UserEditForm
from sqlalchemy.sql import text

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if(current_user.is_authenticated):
        return redirect(url_for("index"))
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
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 
    
@app.route("/auth/new/")
def auth_form():
    if(current_user.is_authenticated):
        return redirect(url_for("index"))
    return render_template("auth/new.html", form = RegisterForm())

@app.route("/auth/<user_id>/")
def auth_profile(user_id):
    stmt = text("SELECT Account.id, Account.username, COUNT(Review.id) FROM Account LEFT JOIN Review ON Account.id = Review.user_id WHERE Account.id = :user_id GROUP BY Account.id").params(user_id=user_id)
    res = db.engine.execute(stmt)
    users = []
    isUser = 0
    for row in res:
        users.append({"id":row[0], "username":row[1], "review_count":row[2]})
        isUser+=1
    if(isUser == 0):
        return render_template("index.html")
    users_id = 0
    if(current_user.is_authenticated):
        users_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :users_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Account.id = :user_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id").params(users_id=users_id, user_id=user_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    
    return render_template("auth/profile.html", users = users, reviews = reviews)

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

@app.route("/auth/<user_id>/delete", methods=["POST"])
@login_required
def auth_delete(user_id):
    if(not current_user.admin):
        if(int(user_id) != int(current_user.id)):
            return render_template("index.html")
    if(not not current_user.admin):
        if(int(user_id) == int(current_user.id)):
            return render_template("index.html")
    if(not current_user.admin):
        logout_user()
    user = User.query.get(user_id)
    likes = Like.query.filter_by(user_id=user.id)
    for like in likes:
        db.session().delete(like)
    reviews = Review.query.filter_by(user_id=user.id)
    for review in reviews:
        likes = Like.query.filter_by(review_id=review.id)
        for like in likes:
            db.session().delete(like)
        db.session().delete(review)
    db.session().delete(user)
    db.session().commit()
    return render_template("index.html")

   
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