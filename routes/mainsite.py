from flask import Blueprint, render_template, request

app_mainsite = Blueprint('mainsite', __name__,
                     url_prefix='/shop/',
                     template_folder='templates/',
                     static_folder='static',
                     static_url_path='assets')

@app_mainsite.route('/teaShop/')
def teaShop():
    return render_template("shop 1.0 smth idk/teaShop.html")

@app_mainsite.route('/teeShop/')
def teeShop():
    return render_template("shop 1.0 smth idk/teeShop.html")

@app_mainsite.route('/nike/')
def nike():
    return render_template("teeShop.html")