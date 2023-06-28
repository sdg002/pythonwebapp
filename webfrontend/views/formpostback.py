import os
from flask import Blueprint, render_template, request
import datetime
import logging
import lib as lib

form_post_back = Blueprint(name="form_post_back", import_name=__name__)

@form_post_back.route("/formpostback", methods=["GET"])
def home_get():
    logging.info("Get handler")
    return render_template("formpostback.html")

@form_post_back.route("/formpostback", methods=["POST"])
def home_submit():
    email=request.form['exampleemail']
    text=request.form['exampletext']
    color=request.form['examplecolor']
    message=f"Form submission ,email={email}, text={text}, color={color}"
    logging.info(message)
    return render_template("formpostback.html", message=message, exampleemail=email, examplecolor=color, exampletext=text)


@form_post_back.route("/formpostbackusinggetmethod", methods=["GET","POST"])
def form_submit_using_get():
    logging.info("Get handler")
    example_color=request.args.get("examplecolor", "")
    color_values=["red", "green", "blue"]
    color_labels = ["Red" ,"Green", "Blue"]
    html_helper = lib.SelectElementHelper(values=color_values, labels=color_labels, selected_value=example_color)

    example_colour=request.args.get("examplecolor", "")
    exampletext=request.args.get("exampletext", "")
    exampleemail = request.args.get("exampleemail", "")
    message=f"<strong>Email</strong>={exampleemail}, <strong>Colour</strong>={example_colour}, <strong>Example text</strong>={exampletext}"
    return render_template("formpostbackget.html", exampletext=exampletext, exampleemail=exampleemail, helper=html_helper, message=message)
