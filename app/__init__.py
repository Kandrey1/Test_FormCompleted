from flask import Flask
from config import Settings


def create_app(config_class=Settings):
    app = Flask(__name__)

    app.config.from_object(config_class)

    return app
