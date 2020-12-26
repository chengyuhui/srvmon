import os, eventlet

from .db import Server
from app import app

from .checkers import handlers


def task_check():
    servers = Server.query.filter_by(enabled=True).all()
    for server in servers:
        if server.should_check():
            handlers[server.mode](server)


def loop_check():
    while True:
        try:
            task_check()
        except Exception as e:
            print(e)
        eventlet.sleep(5)


_is_dev = os.environ.get("FLASK_ENV") == "development"
_is_main = os.environ.get("WERKZEUG_RUN_MAIN") == "true"

# We don't want multiple instances of the scheduler
if (not _is_dev) or (_is_dev and _is_main):
    app.logger.info("Starting scheduler")
    eventlet.spawn_n(loop_check)
