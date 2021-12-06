# flask imports
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
# model imports
from .model import model_create, model_read, model_read_all, model_read_emails, \
    model_read_phones, model_update_name, model_delete, model_read_by_filter

app_mainframe = Blueprint('mainframe', __name__,
                     url_prefix='/mainframe',
                     template_folder='templates/mainframe/',
                     static_folder='static',
                     static_url_path='assets')

@app_mainframe.route('/search')
def mainsearch():
    return render_template("mainframe/full_search.html")

@app_mainframe.route('/search/term/', methods=["POST"])
def search_term():
    req = request.get_json()
    term = req['term']
    query = model_read_by_filter(term) 
    response = make_response(jsonify(query), 200) 
    print(response) 
    return response


