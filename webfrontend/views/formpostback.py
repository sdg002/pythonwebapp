import os
from flask import Blueprint, render_template, request
import datetime
import logging

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
    #you were get values from request and render
    #ammend the HTML to accept parameters
    #render SELECTED item 
    return render_template("formpostbackget.html")
