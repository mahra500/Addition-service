from flask import Flask, request
from blueprints.addition import additon_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(additon_bp.addition_bp)

    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0',  port=5000, debug=True)