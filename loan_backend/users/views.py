from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class SigninRequest(APIView):
    """
    Receive user credentials via the API and
    validate if the user has access.
    """

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Email or password missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        authenticated_user = authenticate(request=request, username=username, password=password)
        if not authenticated_user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_403_FORBIDDEN)

        login(request, authenticated_user)

        token, created_bool = Token.objects.get_or_create(user=authenticated_user)

        authenticated_user.last_login = datetime.now()
        authenticated_user.save()

        response_data = {
            'token': token.key,
            'username': username,
            'id': authenticated_user.id
        }

        return Response(response_data, status=status.HTTP_200_OK)
