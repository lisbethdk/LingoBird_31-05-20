from models.settings import db
from datetime import datetime

from utils.email_helper import send_email


class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    newsletter_email = db.Column(db.String, unique=True)


#@classmethod
#def add(cls, email):
    #newsletter = cls(email=email)
    #db.add(newsletter)
    #db.commit()

 #   if newsletter_email:
  #      send_email(receiver_email=email, subject="Welcome to the LingoBird Family 🐦❤️",
   #                text="Thank you for signing up to our newsletter.")

        #return newsletter
