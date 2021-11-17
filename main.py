# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/everitt/everitthomepage')
def everitt():
    return render_template("everitt/everitthomepage.html")

@app.route('/daniel/home')
def daniel():
    return render_template("daniel/d_homepage.html")

@app.route('/lucas/home')
def lucas():
    return render_template("lucas-templates/l-homepage.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@app.route('/rithwikh/')
def rithwikh():
    return render_template("Rithwikh's Templates/rithwikh.html")

@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
