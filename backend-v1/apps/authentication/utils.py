import logging

from rest_framework.exceptions import ParseError

from ..contrib import constants as constant
from ..contrib.exceptions import InternalServerError
from ..contrib.responses import ResourceCreatedResponse
from ..mails.services import MailService
from ..users.exceptions import UserDoesNotExistException, UserHaveNotConfirmedException
from ..users.models import User

logger = logging.getLogger(__name__)


class ChallengeSwitcher:
    """
    Challenge Switcher
    """

    @classmethod
    def process_challenge(cls, *args, **kwargs):
        try:
            request = kwargs.get('request')
            method_name = '_process_challenge_' + getattr(request, 'data').get('name').lower()
            method = getattr(cls, method_name, lambda: 'Invalid challenge name')
            return method(cls, *args, **kwargs)
        except KeyError as e:
            if e.__str__().replace('\'', '') in ['name']:
                raise ParseError()
            raise InternalServerError()
        except AttributeError as e:
            raise ParseError()
        except Exception as e:
            raise e

    def _process_challenge_forgot_password(self, *args, **kwargs):
        try:
            request = kwargs.get('request')
            username = getattr(request, 'data').get('username')

            user = User.objects.get(username=username)
            user.update_status_force_change_password()
            new_pwd = User.objects.make_random_password(
                length=constant.PASSWORD_MIN_LENGTH, allowed_chars=constant.PASSWORD_ALLOWED_CHARS
            )
            user.save_password(new_pwd)

            mail_service = MailService.get_instance()
            mail_service.send_new_password_mail(email=user.email, password=new_pwd)
        except KeyError as e:
            if e.__str__().replace('\'', '') in ['username']:
                raise ParseError()
            raise InternalServerError()
        except User.DoesNotExist as e:
            raise UserDoesNotExistException()
        except User.NotConfirmed as e:
            raise UserHaveNotConfirmedException()
        except Exception as e:
            raise e
        else:
            return ResourceCreatedResponse()
