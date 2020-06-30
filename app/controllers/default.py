from app import app

@app.route('/index')
@app.route('/')
def index():
    return "Hello World!"

# case name is empty your value now is None
@app.route('/test', defaults={'name': None})
@app.route('/test/<name>')
def test(name):
    if name:
        return "Hello, %s!" % name
    else:
        return "Hello User!"
