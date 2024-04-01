from flask import Flask, render_template, send_from_directory, redirect, jsonify
from PIH_Pune_Price_Pulse import pricepulse
from portfolio import portfolio
import PIH_Pune_Price_Pulse

app = Flask(__name__)
app.register_blueprint(pricepulse.pricepulse, url_prefix="/price-pulse")
app.register_blueprint(portfolio.portfolio, url_prefix="/portfolio")

@app.route('/')
def home():
    return redirect('/portfolio')

@app.route('/keep-alive')
def keep_alive():
    return "Server is alive"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)