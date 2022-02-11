from flask import Blueprint, render_template, request

app_evroutes = Blueprint('evroutes', __name__,
                          url_prefix='/everitt',
                          template_folder='templates/everitt/',
                          static_folder='static',
                          static_url_path='assets')

@app_evroutes.route('/about')
def everitt():
    return render_template("everitt/e_aboutme.html")

@app_evroutes.route('/createtask')
def evcreatetask():
    return render_template("de-createtask.html")