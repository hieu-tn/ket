import logging
from typing import Union

from celery import shared_task
from django.core.mail import EmailMessage

logger = logging.getLogger(__name__)


@shared_task
def send_mail(
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
        logger.info('Sending email {0} to {1}'.format(subject, to))
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


@shared_task
def send_sms(subject: str, body: str, to: str):
    try:
        logger.info('Sending sms {0} to {1}'.format(subject, to))
    except Exception as e:
        raise e
