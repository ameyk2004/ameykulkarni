from flask import Flask, render_template, send_from_directory, Blueprint

pricepulse = Blueprint("pricepulse", __name__, static_folder="static",  template_folder="templates")


@pricepulse.route('/')
def home():
    return render_template('index.html')

@pricepulse.route('/resume')
def resume():
    return render_template('resume.html')

@pricepulse.route('/contact')
def contact():
    return render_template('contact.html')

@pricepulse.route('/projects')
def projects():
    return render_template('projects.html')

@pricepulse.route('/download')
def download_resume():
    return send_from_directory('./resume', 'resume.pdf')
