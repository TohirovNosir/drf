from rest_framework import views
from django.contrib.auth import authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class Login(views.APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["username", "password"],
            example={
                "username": "",
                "password": ""
            }
        ),
        responses={
            200: openapi.Response(description='Success response'),
            400: openapi.Response(description='Bad request'),
        }
    )
    def post(self, request, *args, **kwargs):
        # http://127.0.0.1:8000/api/auth/token/
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_token, created = Token.objects.get_or_create(user=user)
            return Response(auth_token.key)
        return Response({"detail": "user not found"}, status=404)
