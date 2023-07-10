"""Flask entrypoint."""

import os
from typing import Any, Optional

from flask import Flask
from flask_mqtt import Mqtt
from flask_mqtt import M

from webserver.model.db import get_db
from webserver.views.ctrl import ctrl_view_blueprint
from webserver.views.index import index_view_blueprint


class WebserverError(Exception):
    """Webserver Error"""


DEV_SECRET_KEY = "dev"

mqtt: Mqtt = Mqtt()

controllers = {}


def create_app(test_config: Optional[dict[str, Any]] = None) -> Flask:
    """Factory method for creating an application object."""

    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = DEV_SECRET_KEY
    app.config[
        "MQTT_BROKER_URL"
    ] = "localhost"
    app.config["MQTT_BROKER_PORT"] = 1883  # default port for non-tls connection
    app.config[
        "MQTT_USERNAME"
    ] = ""  # set the username here if you need authentication for the broker
    app.config[
        "MQTT_PASSWORD"
    ] = ""  # set the password here if the broker demands authentication
    app.config[
        "MQTT_KEEPALIVE"
    ] = 5  # set the time interval for sending a ping to the broker to 5 seconds
    app.config["MQTT_TLS_ENABLED"] = False  # set TLS to disabled for testing purposes

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    mqtt.init_app(app)

    get_db().init_app(app)

    app.register_blueprint(ctrl_view_blueprint)
    app.register_blueprint(index_view_blueprint)

    return app


@mqtt.on_connect()
def handle_connect():
    """Handle first connection set-up."""
    mqtt.subscribe("ctrl/+/rollcall")

@mqtt.on_topic("ctrl/+/rollcall")
def handle_rollcall_topic(_, __, message):
    """Handle rollcall messages."""
    print(message.payload.decode())
