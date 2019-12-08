from flask import Flask

from .counter import CounterHandler

app = Flask(__name__)


@app.route("/")
def index():
    return str(CounterHandler.get_and_increment_counter())
