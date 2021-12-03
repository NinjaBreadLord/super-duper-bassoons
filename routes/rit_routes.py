import requests

from flask import Blueprint, render_template, request

app_ritroutes = Blueprint('ritroutes', __name__,
                     url_prefix='/rithwikh',
                     template_folder='templates/rithwikh/',
                     static_folder='static',
                     static_url_path='assets')

@app_ritroutes.route('/home')
def rithwikh():

    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

    response = requests.request("GET", url,)

    print(response)

    return render_template("rithwikh/r_homepage.html", response= response)


