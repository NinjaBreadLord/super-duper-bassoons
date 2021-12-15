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

@app_junroutes.route('/api')
def api():
    return render_template("jun/junapi.html")