from logging import getLogger

from cheroot.wsgi import Server

from .settings import SERVER_ADDRESS, SERVER_PORT
from .views import app

LOGGER = getLogger(__name__)


def run_server():
    addr = SERVER_ADDRESS, SERVER_PORT
    server = Server(addr, wsgi_app=app)
    LOGGER.info('Starting server at http://%s:%s', SERVER_ADDRESS, SERVER_PORT)
    server.start()
