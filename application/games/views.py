from application import app, db
from flask_login import login_required
import datetime
from flask import redirect, render_template, request, url_for
from application.games.models import Game
from application.reviews.models import Review
from application.games.forms import GameForm, GameEditForm


@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.order_by(Game.name).all())

@app.route("/games/publicationOrder", methods=["GET"])
def games_publicationList():
    return render_template("games/list.html", games = Game.query.order_by(Game.publication).all())

@app.route("/games/tagOrder", methods=["GET"])
def games_tagList():
    return render_template("games/list.html", games = Game.query.order_by(Game.tag).all())


@app.route("/games/flagged", methods=["GET"])
@login_required
def games_flaggedList():
    return render_template("games/list.html", games = Game.query.filter_by(flag=True).order_by(Game.name))


@app.route("/games/<game_id>/", methods=["POST"])
@login_required
def games_removeOrMarkOrEdit(game_id):
    game = Game.query.get(game_id)
    if('mark' in request.form):
        game.flag = True
    elif('remove' in request.form):
        reviews = Review.query.filter_by(game_id=game.id)
        for review in reviews:
            db.session().delete(review)
        db.session().delete(game)
    elif('edit' in request.form):
        form = GameEditForm()
        form.oldName.data = game.name
        form.name.data = game.name
        form.tag.data = game.tag
        form.publication.data = "{}-{}-{}".format(game.publication.year, game.publication.month, game.publication.day)
        return render_template("games/edit.html", form = form, game = game)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/edit/")
@login_required
def games_edit():
    return render_template("games/edit.html", form = GameEditForm())


@app.route("/games/new/")
@login_required
def games_form():
    return render_template("games/new.html", form = GameForm())

@app.route("/games/", methods=["POST"])
@login_required
def games_createOrUpdate():
    if('create' in request.form):
        form = GameForm(request.form)

        if not form.validate():
            return render_template("games/new.html", form = form)
        name = form.name.data    
        tag = form.tag.data
        year, month, day = map(int, form.publication.data.split('-'))
        publication = datetime.date(year, month, day)
        game = Game(name, tag, publication)
        db.session().add(game)
        db.session().commit()
    elif('edit' in request.form):
        form = GameEditForm(request.form)

        if not form.validate():
            return render_template("games/edit.html", form = form)
        oldName = form.oldName.data
        game = Game.query.filter_by(name=oldName).first()
        
        year, month, day = map(int, form.publication.data.split('-'))
        publication = datetime.date(year, month, day)
        game.name = form.name.data
        game.tag = form.tag.data
        game.flag = False
        game.publication = publication
        db.session().commit()
        
    return redirect(url_for("games_index"))
    
    
    
    