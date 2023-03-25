from flask import render_template
from fly_app import app


@app.route('/')
def main_page():
    return render_template('index.html')