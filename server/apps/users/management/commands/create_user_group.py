from itertools import chain

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError

from ... import constants as users_constant


class Command(BaseCommand):
    help = 'Create user group'

    def handle(self, *args, **options):
        try:
            groups = users_constant.USER_GROUP.list()
            for g in groups:
                method_name = 'get_permissions_for_group_' + g.lower()
                method = getattr(self, method_name)
                permissions = method()
                _, created = Group.objects.get_or_create(
                    name=g,
                    defaults={'permissions': [p.id for p in permissions]},
                )
                if created:
                    self.stdout.write('Inserted {} to auth_group table'.format(g))
                else:
                    self.stdout.write('Existed auth_group {}. No action'.format(g))
        except Exception as e:
            raise CommandError('Error create group {}'.format(e.__repr__()))

    def get_permissions_for_group_end_user(self):
        actions = ['add', 'change', 'view', 'delete']
        app_labels = ['users']
        content_types = self.get_content_types(app_labels)
        permissions = self.get_permissions(content_types, actions)
        return permissions

    def get_permissions_for_group_admin(self):
        actions = []
        app_labels = []
        content_types = self.get_content_types(app_labels)
        permissions = self.get_permissions(content_types, actions)
        return list(chain(self.get_permissions_for_group_end_user(), permissions))

    def get_permissions(self, content_types, actions: list):
        permissions = list()
        for act in actions:
            permissions.extend(
                chain(Permission.objects.filter(content_type_id__in=content_types, codename__contains=act))
            )
        return permissions

    def get_content_types(self, app_labels: list):
        return ContentType.objects.filter(app_label__in=app_labels)
