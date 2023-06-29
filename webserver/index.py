from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class CtrlForm(FlaskForm):
    elevation = IntegerField("elevation", validators=[DataRequired()])
    azimuth = IntegerField("azimuth", validators=[DataRequired()])


ctrl_view_blueprint = Blueprint("ctrl", __name__)


@ctrl_view_blueprint.route("/", methods=("GET", "POST"))
def ctrl():
    form: FlaskForm = CtrlForm()
    return render_template("index.html", form=form)
