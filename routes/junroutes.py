from flask import Blueprint, render_template
import requests
import json
app_junroutes = Blueprint('junroutes', __name__,
                          url_prefix='/jun',
                          template_folder='templates/jun/',
                          static_folder='static',
                          static_url_path='assets')


@app_junroutes.route('/')
def jun():
    return render_template("jun/j_aboutme.html")

@app_junroutes.route('/junapi/', methods=['GET', 'POST'])
def junapi():
    url = "https://quiterandomapi.p.rapidapi.com/api"

    headers = {
        'x-rapidapi-host': "quiterandomapi.p.rapidapi.com",
        'x-rapidapi-key': "9e4650470emshc2461cc01c07b29p18b9b5jsnfa759ab87fca"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.json())
    data = json.loads(response.text)
    return render_template("junapi.html", output=response.json())