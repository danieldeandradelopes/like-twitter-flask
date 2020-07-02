from flask import render_template, flash
from flask_login import login_user
from app import app, db

from app.models.forms import LoginForm
from app.models.tables import User

# @app.route('/index/<user>')
# @app.route('/', defaults={"user": None})
# def index(user):
#     return render_template('index.html', user=user)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in")
        else:
            flash("Invalid login")
    else:
        print(form.errors)
    return render_template('login.html', form=form)


# CREATE
# @app.route('/teste/<info>')
# @app.route('/teste', defaults={"info": None})
# def teste(info):
#     i = User("danieldeandradelopes", "lop32145", "Daniel Lopes",
#              "danieldeandradelopes@gmail.com")
#     db.session.add(i)
#     db.session.commit()

#     return "CREATE"

# READ
# @app.route('/teste/<info>')
# @app.route('/teste', defaults={"info": None})
# def teste(info):
#     r = User.query.filter_by(username="daniel23").all()
#     print(r) 
#     # print(r.username, r.name)
#     return "LISTED"

# UPDATE
# @app.route('/teste/<info>')
# @app.route('/teste', defaults={"info": None})
# def teste(info):
#     r = User.query.filter_by(username="daniel23").first()
#     r.name = "Daniel de Andrade Lopes"
#     db.session.add(r)
#     db.session.commit()

#     return "UPDATED"

# DELETE
# @app.route('/teste/<info>')
# @app.route('/teste', defaults={"info": None})
# def teste(info):
#     r = User.query.filter_by(username="daniel23").first()
#     db.session.delete(r)
#     db.session.commit()

#     return "DELETED"



# HELLO WORLD ROUTE
# case name is empty your value now is None
# @app.route('/test', defaults={'name': None})
# @app.route('/test/<name>')
# def test(name):
#     if name:
#         return "Hello, %s!" % name
#     else:
#         return "Hello User!"
