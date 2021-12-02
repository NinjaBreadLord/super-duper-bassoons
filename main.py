# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

applist = ["apis", "danroutes", "lucroutes", "ritroutes", "junroutes", "evroutes"]

from routes.apis import app_apis
from routes.danroutes import app_danroutes
from routes.lucroutes import app_lucroutes
from routes.ritroutes import app_ritroutes
from routes.junroutes import app_junroutes
from routes.evroutes import app_evroutes

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
