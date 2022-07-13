
import pytest
from rest_framework import status
from django.conf import settings

from url.views import UrlAPIView
from url.models import Url

pytestmark = pytest.mark.django_db


class TestURLShortener:
    """ Contain tests related to the URL generation """

    def test_url_shortener_generation(self, rf):
        """
        Check converting an long URL into a short representation and viceversa

        :param rf: instance of Django test RequestFactory
        :return:
        """

        API = "/api/v1/url_shortener/"
        long_url = "www.google.com"

        data_to_post = {
            "long_url": long_url,
        }

        # Send a POST request to create a short URL representation
        view = UrlAPIView.as_view()
        request = rf.post(
            API,
            data=data_to_post
        )

        # Make sure the request was successful
        view_response = view(request)
        assert view_response.status_code == status.HTTP_201_CREATED

        obtained_short_url = view_response.data

        # Make sure the short URL contains the expected protocol and domain
        assert settings.URL_PROTOCOL in obtained_short_url
        assert settings.URL_DOMAIN in obtained_short_url

        url_obj = Url.objects.filter(short_url=obtained_short_url).first()
        assert url_obj is not None
        assert url_obj.visits_counter == 0

        # Send a GET request to obtain the long URL representation
        view = UrlAPIView.as_view()
        request = rf.get(
            f"{API}?short_url={obtained_short_url}"
        )

        # Make sure the request was successful
        view_response = view(request)
        assert view_response.status_code == status.HTTP_200_OK

        obtained_long_url = view_response.data

        assert obtained_long_url == long_url

        url_obj = Url.objects.filter(short_url=obtained_short_url).first()
        assert url_obj is not None
        assert url_obj.visits_counter == 1
