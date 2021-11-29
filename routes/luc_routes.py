from flask import Blueprint, render_template, request

app_lucroutes = Blueprint('lucroutes', __name__,
                     url_prefix='/lucas',
                     template_folder='templates/lucas/',
                     static_folder='static',
                     static_url_path='assets')

@app_lucroutes.route('/home')
def lucas():
    return render_template("lucas/l_homepage.html")