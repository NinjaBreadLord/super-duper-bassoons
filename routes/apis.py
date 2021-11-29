from flask import Blueprint, render_template, request

app_apis = Blueprint('api', __name__,
                          url_prefix='/api',
                          template_folder='templates/apis/',
                          static_folder='static',
                          static_url_path='assets')
