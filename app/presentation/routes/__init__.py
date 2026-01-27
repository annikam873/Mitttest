import os
from flask import Blueprint, render_template
# Vi hämtar logiken från Business-lagret
from app.business.services.info_service import get_welcome_message, get_processed_tasks

# 1. HÄR definierar vi main_bp (Viktigt att detta ligger ÖVERst!)
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
main_bp = Blueprint('main', __name__, template_folder=template_dir)

# 2. NU kan vi använda main_bp för att skapa rutter
@main_bp.route('/')
def home():
    msg = get_welcome_message()
    tasks_list = get_processed_tasks()
    return render_template('index.html', message=msg, tasks=tasks_list)

@main_bp.route('/om')
def about():
    return render_template('about.html')