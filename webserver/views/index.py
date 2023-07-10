"""Index view for DSES IF controllers"""
from flask import Blueprint, render_template

from webserver.dish import dish_manager

index_view_blueprint = Blueprint("index", __name__)


@index_view_blueprint.route("/", methods=("GET", "POST"))
def index() -> str:
    """Index view"""
    # Issue 2: populate based on rollcall topic
    return render_template("index.html", controllers=dish_manager.controllers)
