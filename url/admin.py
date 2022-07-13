""" Register the URL models into the Django administration """

from django.contrib import admin

from url.models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    """ Register the model with the ModelAdmin, so it is editable in the admin interface """

    list_display = ["id", "short_url", "long_url", "visits_counter"]
    ordering = ["visits_counter"]
    search_fields = ["short_url", "long_url", "visits_counter"]
