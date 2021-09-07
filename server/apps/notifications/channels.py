import logging
from abc import abstractmethod, ABC
from typing import Union

from .tasks import send_mail, send_sms

logger = logging.getLogger(__name__)


class Channel:
    @abstractmethod
    def send(self, *args, **kwargs):
        raise NotImplemented('implement send in {}'.format(self.__class__.__name__))


class MailChannel(Channel):
    def send(
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
            logger.info('Add action send email {subject} to {to} to queue'.format(subject=subject, to=to))
            send_mail.delay(
                subject=subject,
                body=body,
                from_email=from_email,
                to=to,
                bcc=bcc,
                attachments=attachments,
                cc=cc,
                reply_to=reply_to,
            )
        except Exception as e:
            raise e


class SmsChannel(Channel):
    def send(self, subject: str, body: str, to: str):
        try:
            logger.info('Add action send sms {subject} to {to} to queue'.format(subject=subject, to=to))
            send_sms.delay(subject=subject, body=body, to=to)
        except Exception as e:
            raise e
