from application import app, db
from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for
from application.reviews.models import Review
from application.games.models import Game
from application.likes.models import Like
from application.reviews.forms import ReviewForm, ReviewEditForm
from sqlalchemy import desc
from sqlalchemy.sql import text
import os

@app.route("/reviews/game/<game_id>", methods=["POST", "GET"])
def reviews_index(game_id):
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Game.id = :game_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Game.name").params(user_id=user_id, game_id=game_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7]})
    game = Game.query.filter_by(id=game_id).first()
    return render_template("reviews/list.html", reviews = reviews, game = game)

@app.route("/reviews/list", methods=["GET"])
def reviews_list():
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Game.name").params(user_id=user_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    return render_template("reviews/listing.html", reviews = reviews)
    
@app.route("/reviews/listReverse", methods=["GET"])
def reviews_listReverse():
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Game.name DESC").params(user_id=user_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    
    return render_template("reviews/listing.html", reviews = reviews)

@app.route("/reviews/listGradeOrderAsc", methods=["GET"])
def reviews_listGradeOrderAsc():
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Review.grade").params(user_id=user_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    
    return render_template("reviews/listing.html", reviews = reviews)

@app.route("/reviews/listGradeOrderDesc", methods=["GET"])
def reviews_listGradeOrderDesc():
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Review.grade DESC").params(user_id=user_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    
    return render_template("reviews/listing.html", reviews = reviews)

@app.route("/reviews/listLikeOrderAsc", methods=["GET"])
def reviews_listLikeOrderAsc():
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY like_count").params(user_id=user_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    
    return render_template("reviews/listing.html", reviews = reviews)

@app.route("/reviews/listLikeOrderDesc", methods=["GET"])
def reviews_listLikeOrderDesc():
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY like_count DESC").params(user_id=user_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    
    return render_template("reviews/listing.html", reviews = reviews)


@app.route("/reviews/gradeOrderDesc/<game_id>", methods=["GET", "POST"])
def reviews_gameGradeOrderDesc(game_id):
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Game.id = :game_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Review.grade DESC").params(user_id=user_id, game_id=game_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7]})
    
    game = Game.query.filter_by(id=game_id).first()
    return render_template("reviews/list.html", reviews = reviews, game = game)

@app.route("/reviews/gradeOrderAsc/<game_id>", methods=["GET", "POST"])
def reviews_gameGradeOrderAsc(game_id):
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Game.id = :game_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Review.grade").params(user_id=user_id, game_id=game_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7]})
    
    game = Game.query.filter_by(id=game_id).first()
    return render_template("reviews/list.html", reviews = reviews, game = game)    

@app.route("/reviews/likeOrderDesc/<game_id>", methods=["GET", "POST"])
def reviews_gameLikeOrderDesc(game_id):
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Game.id = :game_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY like_count DESC").params(user_id=user_id, game_id=game_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7]})
    
    game = Game.query.filter_by(id=game_id).first()
    return render_template("reviews/list.html", reviews = reviews, game = game)

@app.route("/reviews/likeOrderAsc/<game_id>", methods=["GET", "POST"])
def reviews_gameLikeOrderAsc(game_id):
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Game.id = :game_id GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY like_count").params(user_id=user_id, game_id=game_id)
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7]})
    
    game = Game.query.filter_by(id=game_id).first()
    return render_template("reviews/list.html", reviews = reviews, game = game)  

@app.route("/reviews/flagged", methods=["GET"])
@login_required
def reviews_flaggedList():
    if(not current_user.admin):
        return redirect(url_for("reviews_list"))
    user_id = 0
    if(current_user.is_authenticated):
        user_id = current_user.id
    if os.environ.get("HEROKU"):
        stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Review.flag = True GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Game.name").params(user_id=user_id)
    else: 
        stmt = text("SELECT Review.id, Game.name, Account.username, Review.grade, Review.text, COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id LEFT JOIN Liking ON Review.id = Liking.review_id WHERE Review.flag = 1 GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Game.name").params(user_id=user_id)
    
    
    res = db.engine.execute(stmt)
    reviews = []

    for row in res:         
        reviews.append({"id":row[0], "game_name":row[1], "username":row[2], "grade":row[3], "text":row[4], "like_count":row[5], "is_liked":row[6], "user_id":row[7], "game_id":row[8]})
    return render_template("reviews/listing.html", reviews = reviews)


@app.route("/reviews/<review_id>/mark", methods=["POST"])
@login_required
def reviews_mark(review_id):
    review = Review.query.get(review_id)
    review.flag = True
    
    db.session().commit()
    if('list' in request.form):
        return redirect(url_for("reviews_index", game_id = review.game_id))
    elif('listing' in request.form):
        return redirect(url_for("reviews_list"))
    elif('profile' in request.form):
        return redirect(url_for("auth_profile", user_id = review.user_id))

@app.route("/reviews/<review_id>/unmark", methods=["POST"])
@login_required
def reviews_unmark(review_id):
    if(not current_user.admin):
        return redirect(url_for("reviews_list"))
    review = Review.query.get(review_id)
    review.flag = False
    
    db.session().commit()
    if('list' in request.form):
        return redirect(url_for("reviews_index", game_id = review.game_id))
    elif('listing' in request.form):
        return redirect(url_for("reviews_list"))
    elif('profile' in request.form):
        return redirect(url_for("auth_profile", user_id = review.user_id))
    
@app.route("/reviews/<review_id>/remove", methods=["POST"])
@login_required
def reviews_remove(review_id):
    review = Review.query.get(review_id)
    user_id = review.user_id
    game_id = review.game_id
    if((not current_user.admin) and (current_user.id != review.user_id)):
        return redirect(url_for("reviews_list"))
    
    likes = Like.query.filter_by(review_id=review.id)
    for like in likes:
        db.session().delete(like)
    db.session().delete(review)

    db.session().commit()
    if('list' in request.form):
        return redirect(url_for("reviews_index", game_id = game_id))
    elif('listing' in request.form):
        return redirect(url_for("reviews_list"))
    elif('profile' in request.form):
        return redirect(url_for("auth_profile", user_id = user_id))

@app.route("/reviews/<review_id>/edit", methods=["POST"])
@login_required
def reviews_editReview(review_id):
    review = Review.query.get(review_id)
    form = ReviewEditForm()
    form.game_id.data = review.game_id
    form.review_id.data = review.id
    form.grade.data = review.grade
    form.text.data = review.text
    
    return render_template("reviews/edit.html", form = form, game = Game.query.filter_by(id=review.game_id).first())

@app.route("/reviews/<review_id>/like/", methods=["POST"])
@login_required
def reviews_like(review_id):
    exists = Like.query.filter_by(review_id=review_id, user_id=current_user.id).first()
    if(exists is None):
        like = Like(current_user.id, review_id)
        
        db.session().add(like)
        db.session().commit()
    review = Review.query.get(review_id)
    if('list' in request.form):
        return redirect(url_for("reviews_index", game_id = review.game_id))
    elif('listing' in request.form):
        return redirect(url_for("reviews_list"))
    elif('profile' in request.form):
        return redirect(url_for("auth_profile", user_id = review.user_id))
    
@app.route("/reviews/<review_id>/unlike/", methods=["POST"])
@login_required
def reviews_unlike(review_id):
    exists = Like.query.filter_by(review_id=review_id, user_id=current_user.id).first()
    if(not (exists is None)):
        db.session().delete(exists)
        db.session().commit()
    review = Review.query.get(review_id)
    if('list' in request.form):
        return redirect(url_for("reviews_index", game_id = review.game_id))
    elif('listing' in request.form):
        return redirect(url_for("reviews_list"))
    elif('profile' in request.form):
        return redirect(url_for("auth_profile", user_id = review.user_id))

@app.route("/reviews/edit/")
@login_required
def reviews_edit():
    return render_template("reviews/new.html", form = ReviewEditForm())


@app.route("/reviews/new/<game_id>", methods=["POST"])
@login_required
def reviews_form(game_id):
    form = ReviewForm()
    form.game_id.data = game_id
    return render_template("reviews/new.html", form = form, game = Game.query.filter_by(id=game_id).first())

@app.route("/reviews/", methods=["POST"])
@login_required
def reviews_createOrUpdate():
    if('create' in request.form):
        form = ReviewForm(request.form)

        if not form.validate():
            return render_template("reviews/new.html", form = form, game = Game.query.filter_by(id=form.game_id.data).first())
        game_id = form.game_id.data
        grade = form.grade.data
        text = form.text.data
        
        review = Review(game_id, grade, text)
        review.game_id = game_id
        review.user_id = current_user.id
        
        db.session().add(review)
        db.session().commit()
    elif('edit' in request.form):
        form = ReviewEditForm(request.form)

        if not form.validate():
            return render_template("reviews/edit.html", form = form, game = Game.query.filter_by(id=form.game_id.data).first())
        review_id = form.review_id.data
        review = Review.query.filter_by(id=review_id).first()
        
        review.grade = form.grade.data
        review.text = form.text.data
        
        db.session().commit()
        
    return redirect(url_for("reviews_index", game_id = form.game_id.data))
    
    
    
    