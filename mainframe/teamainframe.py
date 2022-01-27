"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests

from model import Teas

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_teamainframe = Blueprint('teamainframe', __name__,
                     url_prefix='/teamainframe',
                     template_folder='templates/teamainframe/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_teamainframe)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Teas table queries"""


# User/Teas extraction from SQL
def Teas_all():
    """converts Teas table into JSON list """
    return [peep.read() for peep in Teas.query.all()]


def Teas_ilike(term):
    """filter Teas table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Teas.query.filter((Teas.name.ilike(term)) | (Teas.teatype.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def user_by_id(teaID):
    """finds User in table matching teaID """
    return Teas.query.filter_by(teaID=teaID).first()


# User extraction from SQL
def user_by_url(url):
    """finds User in table matching url """
    return Teas.query.filter_by(url=url).first()


""" app route section """


# Default URL
@app_teamainframe.route('/', methods=["GET", "POST"])
def mainframe():
    """obtains all Teas from table and loads Admin Form"""
    if request.form:
        key = request.form.get("key")
        if key == "adminentrance":  # input field has content
            return render_template("teamainframe.html", table=Teas_all())        
    return render_template("teaentry.html", methods=["POST"])


# CRUD create/add
@app_teamainframe.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Teas table"""
    if request.form:
        po = Teas(
            request.form.get("name"),
            request.form.get("url"),
            request.form.get("imgurl"),
            request.form.get("teatype"),
            request.form.get("description"),
        )
        po.create()
    return render_template("teamainframe.html", table=Teas_all())


# CRUD read
@app_teamainframe.route('/read/', methods=["POST"])
def read():
    """gets teaID from form and obtains corresponding data from Teas table"""
    table = []
    if request.form:
        teaID = request.form.get("teaID")
        po = user_by_id(teaID)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("teamainframe.html", table=table)


# CRUD update
@app_teamainframe.route('/update/', methods=["POST"])
def update():
    """gets teaID and name from form and filters and then data in  Teas table"""
    if request.form:
        teaID = request.form.get("teaID")
        name = request.form.get("name")
        po = user_by_id(teaID)
        if po is not None:
            po.update(name)
    return render_template("teamainframe.html", table=Teas_all()) 


# CRUD delete
@app_teamainframe.route('/delete/', methods=["POST"])
def delete():
    """gets teaID from form delete corresponding record from Teas table"""
    if request.form:
        teaID = request.form.get("teaID")
        po = user_by_id(teaID)
        if po is not None:
            po.delete()
    return render_template("teamainframe.html", table=Teas_all()) 


# Search Form
@app_teamainframe.route('/search/')
def search():
    return render_template("full_search.html")


# Search request and response
@app_teamainframe.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    output = Teas_ilike(term)
    output.sort(key=lambda x: x["name"])
    response = make_response(jsonify(output), 200)
    return response


""" API routes section """


class TeasAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, url, description, usertag):
            po = Teas(name, url, description, usertag)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {url} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return Teas_all()

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return Teas_ilike(term)

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
        def delete(self, teaID):
            po = user_by_id(teaID)
            if po is None:
                return {'message': f"{teaID} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    # api.add_resource(_Create, '/create/<string:name>/<string:url>/<string:description>/')
    # api.add_resource(_Read, '/read/')
    # api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    # api.add_resource(_Update, '/update/<string:url>/<string:name>')
    # api.add_resource(_UpdateAll, '/update/<string:url>/<string:name>/<string:description>/')
    # api.add_resource(_Delete, '/delete/<int:teaID>')


""" API testing section """


# def api_tester():
#     # local host URL for model
#     url = 'http://127.0.0.1:5000/mainframe'

#     # test conditions
#     API = 0
#     METHOD = 1
#     tests = [
#         ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
#         ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
#         ['/read/', "get"],
#         ['/read/ilike/John', "get"],
#         ['/read/ilike/com', "get"],
#         ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
#         ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
#         ['/delete/4', "delete"],
#         ['/delete/5', "delete"],
#     ]

#     # loop through each test condition and provide feedback
#     for test in tests:
#         print()
#         print(f"({test[METHOD]}, {url + test[API]})")
#         if test[METHOD] == 'get':
#             response = requests.get(url + test[API])
#         elif test[METHOD] == 'post':
#             response = requests.post(url + test[API])
#         elif test[METHOD] == 'put':
#             response = requests.put(url + test[API])
#         elif test[METHOD] == 'delete':
#             response = requests.delete(url + test[API])
#         else:
#             print("unknown RESTapi method")
#             continue

#         print(response)
#         try:
#             print(response.json())
#         except:
#             print("unknown error")


# def api_printer():
#     print()
#     print("Teas table")
#     for user in Teas_all():
#         print(user)


# """validating api's requires server to be running"""
# if __name__ == "__main__":
#     api_tester()
#     api_printer()