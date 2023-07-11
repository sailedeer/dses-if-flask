"""Controller view for a single DSES IF controller."""
from flask import Blueprint, abort, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

from webserver.dish.dish_controller import dishes


class CtrlForm(FlaskForm):
    """Controller form"""

    elevation = IntegerField("elevation", validators=[DataRequired()], default=0)
    azimuth = IntegerField("azimuth", validators=[DataRequired()], default=0)


ctrl_view_blueprint = Blueprint("ctrl", __name__)


@ctrl_view_blueprint.route("/ctrl/<interferometer_id>", methods=("GET", "POST"))
def ctrl(interferometer_id) -> str:
    """Control view"""
    form: FlaskForm = CtrlForm()
    if interferometer_id not in dishes:
        abort(404)
    if request.method == "POST":
        # Issue #4: publish new position to MQTT server
        print(f"would send azimuth: {form.azimuth.data}")
        print(f"would send elevation: {form.elevation.data}")
    return render_template("ctrl.html", form=form)
