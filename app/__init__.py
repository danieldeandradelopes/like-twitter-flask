from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# created a instance
# configuring migrate 
# receive my app and db in your configurations
migrate = Migrate(app, db)

# received commands of applications
manager = Manager(app)
manager.add_command('db', MigrateCommand)


login_manager =  LoginManager(app)

# USER LOADER => TO LOGIN AND LOGOU 
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

from app.models import tables, forms
from app.controllers import default
