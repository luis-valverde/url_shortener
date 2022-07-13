""" Serialize and deserialize data that corresponds to URLs objects """

from rest_framework import serializers

from url.models import Url


class UrlSerializer(serializers.ModelSerializer):
    """ Specify the serializer for the Url model """

    class Meta:
        """ Specify metadata for the Url serializer """

        model = Url
        fields = "__all__"
