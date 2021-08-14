from django import template
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator


template = "registration/email/new_account.html"


class SendMail(user):
    c = {
        "user": user,
        "email": user.email,
        'domain': 'the-kuks.herokuapp.com'# site url,
        'site_name':'The Kuks',
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
        'protocol':'https',
    }
    def mail(user, c):
        subject = "Account Created"
        plaintext = template.loader.get_template("registration/email/new_account_subject.txt")
        htmltemp = template.loader.get_template("registration/email/new_account.html")
        text_content = plaintext.render(c)
        html_content = htmltemp.render(c)
        try:
            msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=settings.EMAIL_HOST_USER, to=[user.email], headers = {'Reply-To': settings.EMAIL_HOST_USER})
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    def Reset(user):
        subject = "Bevardis Password Reset Requested"
        plaintext = template.loader.get_template("registration/email/password_reset_subject.txt")
        htmltemp = template.loader.get_template("registration/email/password_reset_email.html")
        text_content = plaintext.render(c)
        html_content = htmltemp.render(c)
        try:
            msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=settings.EMAIL_HOST_USER, to=[user.email], headers = {'Reply-To': settings.EMAIL_HOST_USER})
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')