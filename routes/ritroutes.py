from flask import Blueprint, render_template, request
import requests

app_ritroutes = Blueprint('ritroutes', __name__,
                     url_prefix='/rithwikh',
                     template_folder='templates/rithwikh/',
                     static_folder='static',
                     static_url_path='assets')

@app_ritroutes.route('/home')
def rithwikh():
    return render_template("rithwikh/r_homepage.html")

@app_ritroutes.route('/weather')
def weather():
    return render_template("rithwikh/rithwikhAPI.html")


@app_ritroutes.route('/Destiny/')
def Destiny():

    url = "https://destiny-2-xur.p.rapidapi.com/xur"

    headers = {
    'x-rapidapi-host': "destiny-2-xur.p.rapidapi.com",
    'x-rapidapi-key': "9d1b75d842msh20486d8bf8d5c19p1904abjsneb2943a9124c"
    }


    response = requests.request("GET", url, headers=headers)

    print(response.text)

    return render_template("DestinyAPI.html", output=response.json())

@app_ritroutes.route('/create/')
def create():

    url = "https://kohls.p.rapidapi.com/categories/list"

    headers = {
    'x-rapidapi-host': "kohls.p.rapidapi.com",
    'x-rapidapi-key': "9d1b75d842msh20486d8bf8d5c19p1904abjsneb2943a9124c"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    return render_template("rithwikh/CreateTaskRithwikh.html", output=response.json())