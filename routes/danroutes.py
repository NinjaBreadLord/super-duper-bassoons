from flask import Blueprint, render_template, request
import requests

app_danroutes = Blueprint('danroutes', __name__,
                     url_prefix='/daniel',
                     template_folder='templates/daniel/',
                     static_folder='static',
                     static_url_path='assets')

@app_danroutes.route('/home')
def daniel():
    # url = "https://randanimal.pmbytes.org/imageapi/"
    # response = requests.get(url)
    #  api_image=response.text
    return render_template("daniel/d_homepage.html")
    
@app_danroutes.route('/api')
def danielapi():
    return render_template("daniel/api.html")

@app_danroutes.route('/testing1')
def danieltest():
    return render_template("daniel/csstesting.html")

@app_danroutes.route('/createtask')
def dancreatetask():
    return render_template("de-createtask.html")

@app_danroutes.route('/endtest')
def endtest():
    return render_template("daniel/endtest.html")