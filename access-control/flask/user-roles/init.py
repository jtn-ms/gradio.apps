# import Flask from flask
from flask import Flask
# pass current module (__name__) as argument
# this will initialize the instance
 
app = Flask(__name__)


# path to sqlite database
# this will create the db file in instance
# if database not present already
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///g4g.sqlite3"
# needed for session cookies
app.config['SECRET_KEY'] = 'MY_SECRET'
# hashes the password and then stores in the database
app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
# allows new registrations to application
app.config['SECURITY_REGISTERABLE'] = True
# to send automatic registration email to user
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

# import SQLAlchemy for database operations
# and store the instance in 'db'
from flask_sqlalchemy import SQLAlchemy
# Creating an SQLAlchemy instance
db = SQLAlchemy()
db.init_app(app)
 
# import UserMixin, RoleMixin
from flask_security import UserMixin, RoleMixin
 
# create table in database for assigning roles
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))   
 
# create table in database for storing users
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean())
    # backreferences the user_id from roles_users table
    roles = db.relationship('Role', secondary=roles_users, backref='roled')

# create table in database for storing roles
class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)

data = [
    "Admin",
    "Teacher",
    "Staff",
    "Student"
]

app.app_context().push()
db.session.add_all([Role(name=item) for item in data])
db.session.commit()

# def init():
#     with app.app_context():
#         db.session.add_all(data)
#         db.session.commit() 

# init()