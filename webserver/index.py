"""Index view for DSES IF controllers"""
from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class CtrlForm(FlaskForm):
    """Controller form"""
    elevation = IntegerField("elevation", validators=[DataRequired()], default=0)
    azimuth = IntegerField("azimuth", validators=[DataRequired()], default=0)


ctrl_view_blueprint = Blueprint("ctrl", __name__)


@ctrl_view_blueprint.route("/", methods=("GET", "POST"))
def ctrl():
    """Control view"""
    form: FlaskForm = CtrlForm()
    if request.method == "POST":
        print(f"would send azimuth: {form.azimuth.data}")
        print(f"would send elevation: {form.elevation.data}")
    return render_template("index.html", form=form)
