from flask import Flask, render_template, send_from_directory, Blueprint, url_for, redirect
from PIH_Pune_Price_Pulse import pricepulse
from cash_flow_manager import cashflowminimizer

projects = Blueprint("projects", __name__,static_folder="static", template_folder="templates")
projects.register_blueprint(pricepulse.pricepulse, url_prefix="/price-pulse")
projects.register_blueprint(cashflowminimizer.cashflowminimizer, url_prefix="/cash-flow-minimizer")

@projects.route('/')
def home():
    return redirect('/portfolio/projects')

@projects.route('/price-pulse')
def price_pulse_project():
    return redirect('/portfolio')
