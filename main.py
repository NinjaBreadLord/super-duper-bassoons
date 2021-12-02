# import "packages" from flask
from flask import Flask, render_template
import requests
import json

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/everitt/about')
def everitt():
    return render_template("everitt/e_aboutme.html")

@app.route('/daniel/home')
def daniel():
    return render_template("daniel/d_homepage.html")

@app.route('/daniel/testing1')
def danieltest():
    return render_template("daniel/csstesting.html")

@app.route('/rithwikh/home')
def rithwikh():
    return render_template("rithwikh/r_homepage.html")

@app.route('/jun')
def jun():
    return render_template("jun/j_aboutme.html")

@app.route('/junapi/', methods=['GET','POST'])
def junapi():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': "7815f70232mshea0c87cc336b4aap13f459jsn464272722115"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.json())
    data = json.loads(response.text)
    return render_template("junapi.html", output=response.json())

@app.route('/lucas/home')
def lucas():
    return render_template("lucas/l_homepage.html")

# connects /kangaroos path to render kangaroos.html



@app.route('/stub/')
def stub():
    return render_template("stub.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
