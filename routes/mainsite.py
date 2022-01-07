from flask import Blueprint, render_template, request

app_mainsite = Blueprint('mainsite', __name__,
                     url_prefix='/store/',
                     template_folder='templates/',
                     static_folder='static',
                     static_url_path='assets')

@app_mainsite.route('/teaShop/')
def teaShop():
    return render_template("store/teaShop.html")

@app_mainsite.route('/teeShop/')
def teeShop():
    return render_template("store/teeShop.html")

@app_mainsite.route('/nikeShirt/')
def nikeShirt():
    return render_template("store/nikeShirt.html")

@app_mainsite.route('/ShoppingCart/')
def ShoppingCart():
    return render_template("store/shoppingcart.html")