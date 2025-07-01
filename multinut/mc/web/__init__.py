from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import route
    app.register_blueprint(route)
    
    return app
