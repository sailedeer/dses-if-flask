"""Index view for DSES IF controllers"""
from flask import Blueprint, render_template, url_for

from webserver.dish.dish_controller import dishes

index_view_blueprint = Blueprint("index", __name__)


@index_view_blueprint.route("/", methods=("GET", "POST"))
def index() -> str:
    """Index view"""
    # Issue 2: populate based on rollcall topic
    print(
        url_for(
            "ctrl.ctrl", interferometer_id=list(dishes.values())[0].interferometer_id
        )
    )
    return render_template("index.html", controllers=dishes.values())
