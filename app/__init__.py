from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# created a instance
# configuring migrate 
# receive my app and db in your configurations
migrate = Migrate(app, db)

# received commands of applications
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
