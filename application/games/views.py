from application import app, db
import datetime
from flask import redirect, render_template, request, url_for
from application.games.models import Game


@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all())


@app.route("/games/<game_id>/", methods=["POST"])
def games_remove(game_id):
    game = Game.query.get(game_id)
    db.session().delete(game)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/new/")
def games_form():
    return render_template("games/new.html")

@app.route("/games/", methods=["POST"])
def games_create():
    name = request.form.get("name")
    exists = Game.query.filter_by(name=name).first()
    if(exists is None):	
        tag = request.form.get("tag")
        year, month, day = map(int, request.form.get("publication").split('-'))
        publication = datetime.date(year, month, day)
        game = Game(name, tag, publication)
        db.session().add(game)
        db.session().commit()
        return redirect(url_for("games_index"))
    return render_template("games/new.html")        