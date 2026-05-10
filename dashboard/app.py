import os
import sys

from flask import Flask

# Adjust path if running from dashboard dir
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dashboard.routes.api import api_bp
from dashboard.routes.pages import pages_bp


def create_app() -> Flask:
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(pages_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
