from application import app, db
from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for
from application.reviews.models import Review
from application.games.models import Game
from application.reviews.forms import ReviewForm, ReviewEditForm
from sqlalchemy import desc

@app.route("/reviews/<game_id>", methods=["POST", "GET"])
def reviews_index(game_id):
    reviews = Review.query.filter_by(game_id=game_id)
    game = Game.query.filter_by(id=game_id).first()
    return render_template("reviews/list.html", reviews = reviews, game = game)

@app.route("/reviews/list", methods=["GET"])
def reviews_list():
    return render_template("reviews/listing.html", reviews = Review.query.join(Game).order_by(Game.name).all())

@app.route("/reviews/listGrade", methods=["GET"])
def reviews_listGrade():
    return render_template("reviews/listing.html", reviews = Review.query.order_by(desc(Review.grade)).all())


@app.route("/reviews/gradeOrder/<game_id>", methods=["GET", "POST"])
def reviews_gradeOrder(game_id):
    reviews = Review.query.filter_by(game_id=game_id).order_by(desc(Review.grade))
    game = Game.query.filter_by(id=game_id).first()
    return render_template("reviews/list.html", reviews = reviews, game = game)
    

@app.route("/reviews/flagged", methods=["GET"])
@login_required
def reviews_flaggedList():
    return render_template("reviews/listing.html", reviews = Review.query.filter_by(flag=True))


@app.route("/reviews/<review_id>/", methods=["POST"])
@login_required
def reviews_removeOrMarkOrEdit(review_id):
    review = Review.query.get(review_id)
    if('mark' in request.form):
        review.flag = True
    elif('remove' in request.form):
        db.session().delete(review)
    elif('edit' in request.form):
        form = ReviewEditForm()
        form.game_id.data = review.game_id
        form.review_id.data = review.id
        form.grade.data = review.grade
        form.text.data = review.text
        return render_template("reviews/edit.html", form = form, game = Game.query.filter_by(id=review.game_id).first())
    elif('unmark' in request.form):
        review.flag = False
    db.session().commit()
    game = Game.query.filter_by(id=review.game_id).first()
    reviews = Review.query.filter_by(game_id=game.id)
    return render_template("reviews/list.html", reviews = reviews, game = game)

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
        
    return redirect(url_for("games_index"))
    
    
    
    