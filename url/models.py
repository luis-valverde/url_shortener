""" Contain the URLs models for the application """

import uuid
from random import choice

from django.db import models
from django.utils import timezone
from django.conf import settings


class Url(models.Model):
    """ Model use to store information for the shortener URLs """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_url = models.CharField(max_length=50, blank=True, unique=True)
    long_url = models.CharField(max_length=500)
    visits_counter = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def create_short_url(self):
        """
        Create a random short URL

        :return: Random short URL with a specific protocol and domain
        """

        # Generate a random string
        generated_short_url = "".join(
            [choice(settings.URL_CHARACTERS_TO_USE) for _ in range(settings.URL_MAX_LENGTH)]
        )

        return f"{settings.URL_PROTOCOL}://{settings.URL_DOMAIN}/{generated_short_url}"

    def save(self, *args, **kwargs):
        """
        Override default save method to create the instance

        It makes sure a short URL is generated for each instance.

        :param args: arguments of the default save() method
        :param kwargs: keyword arguments of the default save() method
        :return:
        """

        if not self.short_url:
            short_url_exists = True
            generated_short_url = ""

            # Execute until an unique short URL is generated
            while short_url_exists:
                generated_short_url = self.create_short_url()
                short_url_exists = Url.objects.filter(short_url=generated_short_url).exists()

            self.short_url = generated_short_url

        super().save(*args, **kwargs)
