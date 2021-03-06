# import "packages" from flask
from flask import render_template
from __init__ import app
import requests
import json

# create a Flask instance

from routes.apis import app_apis
from routes.danroutes import app_danroutes
from routes.lucroutes import app_lucroutes
from routes.ritroutes import app_ritroutes
from routes.junroutes import app_junroutes
from routes.evroutes import app_evroutes
from mainframe.mainframe import app_mainframe
from mainframe.teamainframe import app_teamainframe
from routes.mainsite import app_mainsite

app.register_blueprint(app_teamainframe)
app.register_blueprint(app_mainframe)
app.register_blueprint(app_mainsite)
app.register_blueprint(app_apis)
app.register_blueprint(app_danroutes)
app.register_blueprint(app_lucroutes)
app.register_blueprint(app_ritroutes)
app.register_blueprint(app_junroutes)
app.register_blueprint(app_evroutes)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
