from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from magicaldayapi.models import Guest, Location

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a guest

    Method arguments:
        request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        user = Guest.objects.get(user_id=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'user': int(user.id)
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new guest for authentication

    Method arguments:
        request -- The full HTTP request object
    '''
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']
    password = request.data['password']
    height = request.data['height']
    profile_picture = request.data['profile_picture']

    
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=email,
        password=password,
        is_staff=False
    )
    guest = Guest.objects.create(
        user=user,
        height=height,
        profile_picture=profile_picture
    )
    token = Token.objects.create(user=user)
    data = {
        'valid': True,
        'token': token.key,
        'user': int(guest.id)
    }
    return Response(data)