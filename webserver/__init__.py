"""Flask entrypoint."""

import os
from typing import Any, Optional

from flask import Flask


class WebserverError(Exception):
    """Webserver Error"""


DEV_SECRET_KEY = "dev"


def create_app(test_config: Optional[dict[str, Any]] = None) -> Flask:
    """Factory method for creating an application object."""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=DEV_SECRET_KEY, DATABASE=os.path.join(app.instance_path, "db.sqlite")
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
