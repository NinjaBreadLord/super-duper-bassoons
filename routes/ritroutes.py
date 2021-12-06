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


