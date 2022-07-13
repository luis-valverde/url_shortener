""" Contain all the API views for URL model """

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from url.models import Url
from url.serializers import UrlSerializer


class UrlAPIView(APIView):
    serializer_class = UrlSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        """
        Take a short URL and obtains the long URL representation and
        increments the number of visits of it.

        :param request: HTTP request object
        :return: Long URL representation, otherwise and exception
        """

        short_url = request.GET.get("short_url", "")
        url_obj = Url.objects.filter(short_url=short_url).first()

        if not url_obj:
            return Response(
                {"message": f"Could not find representation for: {short_url}"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Update the short URL visits number
        url_obj.visits_counter += 1
        url_obj.save()

        return Response(
            url_obj.long_url,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Take a long URL and generates a short URL representation and
        save both fields into the DB.

        :param request: HTTP request object
        :return: Generated short URL, otherwise and exception
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data.get("short_url"),
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
