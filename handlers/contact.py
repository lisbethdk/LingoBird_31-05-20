import hashlib
import uuid
import sqlite3
import datetime

from flask import Flask, render_template, request, redirect, session, url_for, make_response, Blueprint

from models.contact import Contact
from models.user import User
from models.settings import db

contact_handlers = Blueprint("contact", __name__)


@contact_handlers.route("/contact", methods=["GET", "POST"])  # CONTROLLER
def contact():
    session_token = request.cookies.get("session_token")
    user = db.query(User).filter_by(session_token=session_token).first()
    print(user)

    if request.method == "GET":
        session_token = request.cookies.get("session_token")
        user = db.query(User).filter_by(session_token=session_token).first()

        # username = request.cookies.get("username")
        # print(username)
        return render_template("contact.html", user=user)

    elif request.method == "POST":

        contact_name = request.form.get("contact_name")
        contact_email = request.form.get("contact_email")
        contact_message = request.form.get("contact_message")

        contact = Contact(contact_name=contact_name, session_token=str(uuid.uuid4()), contact_email=contact_email,
                          contact_message=contact_message)

        db.add(contact)
        db.commit()

        print(contact_name)
        print(contact_email)
        print(contact_message)

        # Response definieren
        response = redirect(url_for('contact.success', contact=contact, user=user))
        # Cookies setzen
        response.set_cookie("session_token", contact.session_token, httponly=True, samesite='Strict')

        return response  # VIEW


@contact_handlers.route("/success")  # CONTROLLER
def success():
    # Session_Token abfragen
    session_token = request.cookies.get("session_token")
    user = db.query(Contact).filter_by(session_token=session_token).first()

    return render_template("success.html", user=user)
