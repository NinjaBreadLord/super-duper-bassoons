from flask import Blueprint, render_template, request

app_mainframe = Blueprint('mainframe', __name__,
                     url_prefix='/mainframe',
                     template_folder='templates/mainframe/',
                     static_folder='static',
                     static_url_path='assets')

@app_mainframe.route('/search')
def mainsearch():
    return render_template("mainframe/full_search.html")

@app_mainframe.route('/search/term')
def termsearch():
    
    return render_template("mainframe/full_search.html")


