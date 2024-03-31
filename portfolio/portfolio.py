from flask import Flask, render_template, send_from_directory, Blueprint, url_for

portfolio = Blueprint("portfolio", __name__,static_folder="static", template_folder="templates")
@portfolio.route('/')
def home():
    return render_template('home.html')

@portfolio.route('/resume')
def resume():
    return render_template('resume.html')

@portfolio.route('/contact')
def contact():
    return render_template('contact.html')

@portfolio.route('/projects')
def projects():
    return render_template('projects.html')

@portfolio.route('/download')
def download_resume():
    return send_from_directory('static', 'resume/resume.pdf')