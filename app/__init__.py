from flask import Flask, render_template, send_from_directory, redirect, jsonify
from portfolio import portfolio
from projects import projects


def create_app():
    app = Flask(__name__)

    app.register_blueprint(portfolio.portfolio, url_prefix="/portfolio")
    app.register_blueprint(projects.projects, url_prefix="/projects")

    @app.route('/')
    def home():
        return redirect('/portfolio')

    @app.route('/keep-alive')
    def keep_alive():
        return "Server is alive"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80)



