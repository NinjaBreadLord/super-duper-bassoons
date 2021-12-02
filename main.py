# import "packages" from flask
from flask import Flask, render_template
import requests
import json

# create a Flask instance
app = Flask(__name__)

from routes.apis import app_apis
from routes.dan_routes import app_danroutes
from routes.luc_routes import app_lucroutes
from routes.rit_routes import app_ritroutes
from routes.jun_routes import app_junroutes
from routes.ev_routes import app_evroutes

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


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
