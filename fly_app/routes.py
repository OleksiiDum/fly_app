from flask import render_template, url_for
from fly_app import app
from fly_app.controllers import create_airport, get_all_airports


@app.route('/')
def main_page():
    all_airports = get_all_airports()
    return render_template('index.html', airports=all_airports)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/add_airport', methods=["POST"])
def add_airport():
    return create_airport()