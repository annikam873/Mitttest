import os
from flask import Blueprint, render_template, request, redirect, url_for
from app.business.services.info_service import get_welcome_message, get_processed_tasks, add_new_task

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
main_bp = Blueprint('main', __name__, template_folder=template_dir)

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    # Om användaren klickar på "Lägg till" (skickar formuläret)
    if request.method == 'POST':
        new_item = request.form.get('task')
        add_new_task(new_item)
        return redirect(url_for('main.home'))

    # Om användaren bara besöker sidan (vanlig GET)
    msg = get_welcome_message()
    tasks_list = get_processed_tasks()
    return render_template('index.html', message=msg, tasks=tasks_list)

@main_bp.route('/om')
def about():
    return render_template('about.html')