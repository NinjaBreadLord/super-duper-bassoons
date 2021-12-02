from flask import Blueprint, render_template, request
import requests

app_danroutes = Blueprint('danroutes', __name__,
                     url_prefix='/daniel',
                     template_folder='templates/daniel/',
                     static_folder='static',
                     static_url_path='assets')

@app_danroutes.route('/home')
def daniel():
    return render_template("daniel/d_homepage.html")

@app_danroutes.route('/api')
def danielapi():
    url = "https://randanimal.pmbytes.org/imageapi/"
    response = requests.get(url)
    return render_template("daniel/api.html", api_image=response.text)

@app_danroutes.route('/testing1')
def danieltest():
    return render_template("daniel/csstesting.html")