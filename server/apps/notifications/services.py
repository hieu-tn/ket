import logging
from abc import abstractmethod
from typing import Union

from . import constants as notification_constant
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
            content = self.get_content(self.mail_template, self.prepare_mail_data())
        except Exception as e:
            raise e

    def send_sms(self):
        try:
            pass
        except Exception as e:
            raise e

    def get_content(self, template: str, data: dict):
        try:
            logger.info('Get template {}'.format(template))
            # tmpl =
        except Exception as e:
            raise e


class Notification:
    _user = None

    @property
    def user(self):
        return self._user

    @classmethod
    def send(cls, user: Union[User], notification: NotificationActions):
        cls._user = cls.User(user)
        return notification

    class User:
        email = None
        phone = None

        def __init__(self, user):
            if isinstance(user, User):
                self.email = user.email
                self.phone = user.phone
            else:
                self.email = user['email']
                self.phone = user['phone']


class VerificationNotification(Notification, NotificationActions):
    _mail_template = ''
    _sms_template = ''
    code = None

    def __init__(self, code=None):
        self.code = code

    def prepare_mail_data(self):
        pass

    def prepare_sms_data(self):
        pass
