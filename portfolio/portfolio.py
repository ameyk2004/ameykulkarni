from flask import Flask, render_template, send_from_directory, Blueprint, url_for
import os

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

@portfolio.route('/scalp-smart')
def scalp_smart():
    return render_template('scalpsmart.html')

@portfolio.route('/download')
def download_resume():
    cwd = os.getcwd()
    return send_from_directory(f'{cwd}/portfolio/static/resume', 'Amey Kulkarni - Resume.pdf')