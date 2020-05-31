import hashlib
import uuid
import sqlite3
import datetime

from flask import Flask, render_template, request, session, redirect, session, url_for, make_response, Blueprint, flash

from models.user import User
from models.newsletter import Newsletter
from models.settings import db
from utils.email_helper import send_email

newsletter_signup_handlers = Blueprint("newsletter_signup", __name__)


@newsletter_signup_handlers.route("/newsletter", methods=["GET", "POST"])
def newsletter_signup():
    if request.method == "GET":
        session_token = request.cookies.get("session_token")
        user = db.query(User).filter_by(session_token=session_token).first()

        return render_template("newsletter.html", user=user)

    elif request.method == "POST":

        session_token = request.cookies.get("session_token")
        user = db.query(User).filter_by(session_token=session_token).first()

        newsletter_email = request.form.get("newsletter_email")

        signedup_user = db.query(User).filter_by(email=newsletter_email).first()

        if signedup_user:
            flash("This E-Mail address is already signed up for our newsletter.")

            return redirect(url_for('newsletter_signup.newsletter_signup'))

        else:

            newsletter_data = Newsletter(newsletter_email=newsletter_email)

            db.add(newsletter_data)
            db.commit()

            if newsletter_email:
                send_email(receiver_email=newsletter_email, subject="Welcome to the LingoBird Family 🐦❤️",
                           text="Thank you for signing up to our newsletter.")

            response = make_response(redirect(url_for('newsletter_signup.newsletter_success',
                                                      newsletter_email=newsletter_email, user=user)))

            return response


@newsletter_signup_handlers.route("/newsletter-success", methods=["GET", "POST"])
def newsletter_success():
    session_token = request.cookies.get("session_token")
    user = db.query(User).filter_by(session_token=session_token).first()

    return render_template("newsletter-success.html", user=user)
