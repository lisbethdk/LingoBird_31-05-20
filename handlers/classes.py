import uuid
import sqlite3
import datetime

from flask import Flask, render_template, request, session, redirect, url_for, make_response, Blueprint

classes_handlers = Blueprint("classes", __name__)


@classes_handlers.route("/community")  # CONTROLLER
def classes():
    return render_template("classes.html")  # VIEW
