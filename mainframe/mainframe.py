"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests

from model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_mainframe = Blueprint('mainframe', __name__,
                     url_prefix='/mainframe',
                     template_folder='templates/mainframe/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_mainframe)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def users_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Users.query.all()]


def users_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users.query.filter((Users.name.ilike(term)) | (Users.url.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def user_by_id(userid):
    """finds User in table matching userid """
    return Users.query.filter_by(userID=userid).first()


# User extraction from SQL
def user_by_url(url):
    """finds User in table matching url """
    return Users.query.filter_by(url=url).first()


""" app route section """


# Default URL
@app_mainframe.route('/', methods=["GET", "POST"])
def mainframe():
    """obtains all Users from table and loads Admin Form"""
    if request.form:
        key = request.form.get("key")
        if key == "adminentrance":  # input field has content
            return render_template("mainframe.html", table=users_all())        
    return render_template("entry.html", methods=["POST"])


# CRUD create/add
@app_mainframe.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Users(
            request.form.get("name"),
            request.form.get("url"),
            request.form.get("description"),
            request.form.get("usertag")
        )
        po.create()
    return render_template("mainframe.html", table=users_all())


# CRUD read
@app_mainframe.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("mainframe.html", table=table)


# CRUD update
@app_mainframe.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return render_template("mainframe.html", table=users_all()) 


# CRUD delete
@app_mainframe.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            po.delete()
    return render_template("mainframe.html", table=users_all()) 


# Search Form
@app_mainframe.route('/search/')
def search():
    return render_template("full_search.html")


# Search request and response
@app_mainframe.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    output = users_ilike(term)
    output.sort(key=lambda x: x["name"])
    response = make_response(jsonify(output), 200)
    return response


""" API routes section """


class UsersAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, url, description, usertag):
            po = Users(name, url, description, usertag)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {url} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return users_all()

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return users_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, url, name):
            po = user_by_url(url)
            if po is None:
                return {'message': f"{url} is not found"}, 210
            po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, url, name, description, usertag):
            po = user_by_url(url)
            if po is None:
                return {'message': f"{url} is not found"}, 210
            po.update(name, description, usertag)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:url>/<string:description>/<string:usertag>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:url>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:url>/<string:name>/<string:description>/<string:usertag>')
    api.add_resource(_Delete, '/delete/<int:userid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://127.0.0.1:5000/mainframe'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/delete/5', "delete"],
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for user in users_all():
        print(user)


# """validating api's requires server to be running"""
# if __name__ == "__main__":
#     api_tester()
#     api_printer()