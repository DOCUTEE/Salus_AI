from flask import Flask
from .gemini_config import configure_gemini

def create_app():
    app = Flask(__name__)
    configure_gemini()

    from app.routes.food import food_bp
    from app.routes.chat import chat_bp

    app.register_blueprint(food_bp, url_prefix='/api')
    app.register_blueprint(chat_bp, url_prefix='/api')

    return app
