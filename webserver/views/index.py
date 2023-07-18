"""Index view for DSES IF controllers"""
from flask import Blueprint, render_template

from webserver.dish.dish_controller import dishes

index_view_blueprint = Blueprint("index", __name__)


@index_view_blueprint.route("/", methods=("GET", "POST"))
def index() -> str:
    """Index view"""
    return render_template("index.html", controllers=dishes.values())
