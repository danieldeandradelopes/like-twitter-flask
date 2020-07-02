from flask import render_template
from app import app
from app.models.forms import LoginForm

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
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)


# case name is empty your value now is None
# @app.route('/test', defaults={'name': None})
# @app.route('/test/<name>')
# def test(name):
#     if name:
#         return "Hello, %s!" % name
#     else:
#         return "Hello User!"
