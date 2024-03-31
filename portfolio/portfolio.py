from flask import Flask, render_template, send_from_directory
from PIH_Pune_Price_Pulse import pricepulse
import PIH_Pune_Price_Pulse

app = Flask(__name__)
app.register_blueprint(pricepulse.pricepulse, url_prefix="/price-pulse")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/download')
def download_resume():
    return send_from_directory('portfolio/resume', 'resume.pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)