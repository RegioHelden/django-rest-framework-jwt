from six import string_types

from django.apps import apps
from django.contrib.auth import get_user_model as _get_user_model
from django.contrib.auth.models import AbstractUser

from rest_framework import serializers


class Serializer(serializers.Serializer):
    @property
    def object(self):
        return self.validated_data

    @property
    def user_model(self):
        view = self.context.get('view')
        return getattr(view, 'user_model', None)


class PasswordField(serializers.CharField):

    def __init__(self, *args, **kwargs):
        if 'style' not in kwargs:
            kwargs['style'] = {'input_type': 'password'}
        else:
            kwargs['style']['input_type'] = 'password'
        super(PasswordField, self).__init__(*args, **kwargs)


def get_user_model(user_model=None):
    if not user_model:
        return _get_user_model()
    elif isinstance(user_model, string_types):
        return apps.get_model(user_model)
    elif issubclass(user_model, AbstractUser):
        return user_model


def get_username_field(user_model=None):
    return getattr(get_user_model(user_model), 'USERNAME_FIELD', 'username')


def get_username(user):
    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    return username
