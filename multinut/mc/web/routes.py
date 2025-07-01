from flask import Blueprint

route = Blueprint('route', __name__)

@route.route('/')
def index():
    return 'Hello, World!'
