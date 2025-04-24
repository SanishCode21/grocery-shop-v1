from flask import Flask
from models import db
from api import api

app = None

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Grocery_store.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'adsfdf242y6t65fhgsoowqqe'
    db.init_app(app)
    api.init_app(app)
    app.app_context().push()
    return app

app = create_app()

import models
from api import *
import routes



if __name__ == '__main__':
    app.run(debug=True)  #type: ignore
