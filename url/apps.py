""" Deal with the application configuration of the URL app """

from django.apps import AppConfig


class UrlConfig(AppConfig):
    """ Application configuration of the URL app """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'url'
