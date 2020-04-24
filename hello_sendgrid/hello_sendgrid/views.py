import os

from django.http import HttpResponse

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (From, To, PlainTextContent, HtmlContent, Mail)

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
TICO_DEV_GMAIL = os.environ.get('TICO_DEV_GMAIL')
TICO_CHURCH_EMAIL = os.environ.get('TICO_CHURCH_EMAIL')

def index(request):
    sendgrid_client = SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = From(TICO_CHURCH_EMAIL)
    to_email = To(TICO_DEV_GMAIL)
    subject = 'Check Out This SendGrid Magic!'
    plain_text_content = PlainTextContent(
        'How dope is this?'
    )
    html_content = HtmlContent(
        '<strong>It is SO dope!</strong>'
    )
    message = Mail(from_email, to_email, subject, plain_text_content, html_content)
    response = sendgrid_client.send(message=message)

    return HttpResponse('Email Sent!')