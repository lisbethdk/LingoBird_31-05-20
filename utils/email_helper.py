import json
import os
import requests


def send_email(receiver_email, subject, text):
    sender_email = os.getenv("MY_SENDER_EMAIL")  # Your website's official email address
    api_key = os.getenv('SENDGRID_API_KEY')

    if sender_email and api_key:
        url = "https://api.sendgrid.com/v3/mail/send"

        data = {"personalizations": [{
            "to": [{"email": receiver_email}],
            "subject": "Welcome to the LingoBird Family 🐦❤️"
        }],

            "from": {"email": sender_email},

            "template_id": "d-b1fdcc619fc24638b25d122a0a8d0740",

            "content": [{
                "type": "text/html",
                "value": "<html><p>"
            }]

        }

        headers = {
            'authorization': "Bearer {0}".format(api_key),
            'content-type': "application/json"
        }

        # template_id = "d-b1fdcc619fc24638b25d122a0a8d0740"

        response = requests.request("POST", url=url, data=json.dumps(data), headers=headers)

        print("Sent to SendGrid")
        print(response.text)
    else:
        print("No env vars or no email address")
