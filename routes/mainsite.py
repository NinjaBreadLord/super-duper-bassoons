from flask import Blueprint, render_template, request
import json 

from model import Teas

app_mainsite = Blueprint('mainsite', __name__,
                     url_prefix='/store/',
                     template_folder='templates/',
                     static_folder='static',
                     static_url_path='assets')

def Teas_all():
    """converts Teas table into JSON list """
    return [peep.read() for peep in Teas.query.all()]

@app_mainsite.route('/teaShop/')
def teaShop():
    tealist = json.load(open('static/teas.json'))
    return render_template("store/teaShop/teaShop.html", tealist=tealist, table=Teas_all())

@app_mainsite.route('/TeeeShop/')
def TeeeShop():
    teeelist = json.load(open('static/teee.json'))
    return render_template("store/teeeShop.html", teeelist=teeelist)

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

@app_mainsite.route('/LongShirt/')
def LongShirt():
    return render_template("store/longShirt.html")

@app_mainsite.route('/snake/')
def snake():
    return render_template("snake.html")

