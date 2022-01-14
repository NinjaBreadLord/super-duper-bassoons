from flask import Blueprint, render_template, request
import json 

app_mainsite = Blueprint('mainsite', __name__,
                     url_prefix='/store/',
                     template_folder='templates/',
                     static_folder='static',
                     static_url_path='assets')

@app_mainsite.route('/teaShop/')
def teaShop():
    tealist = json.load(open('static/teas.json'))
    return render_template("store/teaShop.html", tealist=tealist)

@app_mainsite.route('/teeShop/')
def teeShop():
    return render_template("store/teeShop.html")

@app_mainsite.route('/nikeShirt/')
def nikeShirt():
    return render_template("store/nikeShirt.html")

@app_mainsite.route('/ShoppingCart/')
def ShoppingCart():
    return render_template("store/shoppingcart.html")

@app_mainsite.route('/Flannels/')
def Flannel():
    return render_template("store/flannelShirt.html")

@app_mainsite.route('/Turtlenecks/')
def Turtlenecks():
    return render_template("store/turtleneck.html")

@app_mainsite.route('/Cart/')
def Cart():
    return render_template("store/Cart.html")

