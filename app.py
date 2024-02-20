from flask import Flask, render_template
from models import User, Section, Book, Rating, Role
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user
from flask_security import Security, SQLAlchemySessionUserDatastore

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def home():
    return render_template('hero.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/lib_signin')
def lib_signin():
    return render_template('lib_signin.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/userview')
def userview():
    return render_template('userview.html')

@app.route('/libview')
def libview():
    return render_template('libview.html')


if __name__ == '__main__':
    app.run(debug=True)