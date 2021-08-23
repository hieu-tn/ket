import logging
from abc import abstractmethod
from typing import Union

from django.template.loader import render_to_string

from . import constants as notification_constant
from .channels import MailChannel
from .exceptions import InvalidChannelException
from ..users.models import User

logger = logging.getLogger(__name__)


class NotificationActions:
    _mail_template = None
    _sms_template = None

    @property
    def mail_template(self):
        return self._mail_template

    @property
    def sms_template(self):
        return self._sms_template

    @abstractmethod
    def prepare_mail_data(self):
        raise NotImplemented('implement {0} in {1}'.format('prepare_mail_data', self.__class__.__name__))

    @abstractmethod
    def prepare_sms_data(self):
        raise NotImplemented('implement {0} in {1}'.format('prepare_mail_data', self.__class__.__name__))

    def via(self, channel: notification_constant.CHANNEL = None):
        try:
            if not channel:
                channel = notification_constant.CHANNEL.MAIL

            method_name = 'send_' + channel.value.lower()
            method = getattr(self, method_name)
            method()
        except AttributeError as e:
            raise InvalidChannelException(e)
        except Exception as e:
            raise e

    def send_mail(self):
        try:
            data = self.prepare_mail_data()
            logger.info('Send mail template {0} with data {1}'.format(self.mail_template, data))
            content = self.get_content(self.mail_template, data.get('context'))
            MailChannel().send(
                subject=data.get('configurations').get('subject'),
                body=content,
                from_email=data.get('configurations').get('from_email'),
                to=data.get('configurations').get('to'),
                bcc=data.get('configurations').get('bcc'),
                attachments=data.get('configurations').get('attachments'),
                cc=data.get('configurations').get('cc'),
                reply_to=data.get('configurations').get('reply_to'),
            )
        except Exception as e:
            raise e

    def send_sms(self):
        try:
            pass
        except Exception as e:
            raise e

    def get_content(self, template: str, data: dict):
        try:
            return render_to_string(template, data)
        except Exception as e:
            raise e


class Notification:
    _user = None

    @property
    def user(self):
        return self._user

    @classmethod
    def send(cls, user: Union[User, dict], notification: NotificationActions):
        cls._user = cls.User(user)
        return notification

    class User:
        mail = None
        phone = None

        def __init__(self, user: Union[User, dict]):
            if isinstance(user, User):
                self.mail = user.email
                self.phone = user.phone
            else:
                self.mail = user.get('mail')
                self.phone = user.get('phone')


class VerificationNotification(Notification, NotificationActions):
    _mail_template = 'mails/verification.html'
    _sms_template = 'sms/verification.txt'
    code = None

    def __init__(self, code=None):
        self.code = code

    def prepare_mail_data(self):
        return {
            'context': {
                'mail': self.user.mail,
                'code': self.code,
            },
            'configurations': {
                'subject': 'Verification code',
                'to': [self.user.mail],
            },
        }

    def prepare_sms_data(self):
        return {
            'code': self.code,
        }
