from django.core.mail import EmailMessage


def send_mail(subject, message, to_emails, attachments=None):
    try:
        email = EmailMessage(subject=subject, body=message, to=to_emails, attachments=attachments)
        email.send()
    except Exception as e:
        print(e)
        raise e
