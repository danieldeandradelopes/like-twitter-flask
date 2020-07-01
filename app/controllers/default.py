from flask import render_template
from app import app


@app.route('/index/<user>')
@app.route('/', defaults={"user": None})
def index(user):
    return render_template('base.html', user=user)

# case name is empty your value now is None
# @app.route('/test', defaults={'name': None})
# @app.route('/test/<name>')
# def test(name):
#     if name:
#         return "Hello, %s!" % name
#     else:
#         return "Hello User!"
