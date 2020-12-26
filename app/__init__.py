from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='../dist')

from .config import Config
app.logger.info('FLASK_ENV = {}'.format(Config.FLASK_ENV))

from . import cron
from .db import db, migrate
from .security import security
from .mail import mail
from .api import api_bp
from .socketio import socketio

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index_client():
    return app.send_static_file('index.html')
