from application import app, db
from flask_login import login_required, current_user
import datetime
from flask import redirect, render_template, request, url_for
from application.games.models import Game
from application.reviews.models import Review
from application.games.forms import GameForm, GameEditForm
from sqlalchemy.sql import text
import os

@app.route("/games", methods=["GET"])
def games_index():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY Game.name")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)
    
@app.route("/gamesReverse", methods=["GET"])
def games_indexReverse():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY Game.name DESC")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)

@app.route("/games/publicationOrder", methods=["GET"])
def games_publicationOrder():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY Game.publication")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)

@app.route("/games/publicationOrderReverse", methods=["GET"])
def games_publicationOrderReverse():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY Game.publication DESC")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)


@app.route("/games/reviewAverageOrderDesc", methods=["GET"])
def games_reviewAverageOrderDesc():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY review_average DESC")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)

@app.route("/games/reviewAverageOrderAsc", methods=["GET"])
def games_reviewAverageOrderAsc():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY review_average")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)

@app.route("/games/reviewCountOrderDesc", methods=["GET"])
def games_reviewCountOrderDesc():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY review_count DESC")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)

@app.route("/games/reviewCountOrderAsc", methods=["GET"])
def games_reviewCountOrderAsc():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY review_count")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)


@app.route("/games/tagOrder", methods=["GET"])
def games_tagOrder():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY Game.tag")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)

@app.route("/games/tagOrderReverse", methods=["GET"])
def games_tagOrderReverse():
    stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average FROM Game LEFT JOIN Review ON Game.id = Review.game_id GROUP BY Game.id ORDER BY Game.tag DESC")
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)


@app.route("/games/flagged", methods=["GET"])
@login_required
def games_flaggedList():
    if(not current_user.admin):
        return redirect(url_for("games_index"))
    stmt = ""
    if os.environ.get("HEROKU"):
        stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average, Game.flag FROM Game LEFT JOIN Review ON Game.id = Review.game_id WHERE Game.flag = True GROUP BY Game.id ORDER BY Game.name")
    else:
        stmt = text("SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average, Game.flag FROM Game LEFT JOIN Review ON Game.id = Review.game_id WHERE Game.flag = 1 GROUP BY Game.id ORDER BY Game.name")   
    res = db.engine.execute(stmt)
    games = []

    for row in res:
        publication_date = ""
        publication = ""
        try:          
            publication_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        except:
            publication_date = row[3]
            publication = "{}.{}.{}".format(publication_date.day, publication_date.month, publication_date.year)
        average = str(row[5])
        if("None" in average):
            average = "0"
        games.append({"id":row[0], "name":row[1], "tag":row[2], "publication":publication, "review_count":row[4], "review_average":average})
    return render_template("games/list.html", games = games)

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
    if(not current_user.admin):
        return redirect(url_for("games_index"))
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
    
    
    
    