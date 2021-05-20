import os
from typing import Union

from django.core.mail import EmailMessage
from django.template.loader import get_template


class MailService:
    """
    Mail Service Singleton
    """

    __instance = None

    def __init__(self):
        """Virtually private constructor."""
        if MailService.__instance is not None:
            raise Exception('This class {} is a singleton!'.format('MailService'))

        MailService.__instance = self

    @staticmethod
    def get_instance():
        """Static access method."""
        if MailService.__instance is None:
            MailService()

        return MailService.__instance

    def send_signup_verification_mail(self, email: str, **kwargs):
        try:
            template = get_template('signup_verification.html')
            context = {'email': email, 'code': kwargs.get('token')}
            content = template.render(context)
            self.send_mail(
                subject='Verification code',
                body=content,
                from_email=kwargs.get('from_email'),
                to=[email],
                bcc=kwargs.get('bcc'),
                attachments=kwargs.get('attachments'),
                cc=kwargs.get('cc'),
                reply_to=kwargs.get('reply_to'),
            )
        except Exception as e:
            raise e

    def send_mail(
        self,
        subject: str,
        body: str,
        from_email: Union[str, None],
        to: Union[list, tuple],
        bcc: Union[list, tuple, None],
        attachments: list,
        cc: Union[list, tuple, None],
        reply_to: Union[list, tuple, None],
    ):
        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=to,
                bcc=bcc,
                attachments=attachments,
                cc=cc,
                reply_to=reply_to,
            )
            email.content_subtype = 'html'
            email.send()
        except Exception as e:
            raise e
