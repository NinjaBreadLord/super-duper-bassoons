""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    url = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    usertag = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, url, description, usertag):
        self.name = name
        self.url = url
        self.description = description
        self.usertag = usertag

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "url": self.url,
            "description": self.description,
            "usertag": self.usertag
        }

    # CRUD update: updates users name, description, usertag
    # returns self
    def update(self, name, description="", usertag=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(description) > 0:
            self.description = description
        if len(usertag) > 0:
            self.usertag = usertag
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Home', url='/', description='The home page of the website.', usertag="Main")
    u2 = Users(name='Daniel - About Me', url='/daniel/home', description='Home and about me page for Daniel Tsivkovski', usertag="Daniel")
    u3 = Users(name='Everitt - About Me', url='/everitt/home', description='Home and about me page for Everitt Cheng', usertag="Everitt")
    u4 = Users(name='Lucas - About Me', url='/lucas/home', description='Home and about me page for Lucas Ho', usertag="Lucas")
    u5 = Users(name='Rithwikh - About Me', url='/rithwikh/home', description='Home and about me page for Rithwikh Varma', usertag="Rithwikh")
    u6 = Users(name='Jun - About Me', url='/rithwikh/home', description='Home and about me page for Jun Lim', usertag="Jun")
    u7 = Users(name='Github', url='https://github.com/NinjaBreadLord/super-duper-bassoons', description='Our GitHub page for this project.', usertag="Main")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate url, or error: {row.url}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()