from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ValidationError
from users.middleware.permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from .serializers.common import UserSerializer
import jwt
from django.conf import settings
from datetime import datetime, timedelta

User = get_user_model()

class RegisteredView(APIView):

    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, 201)
        return Response(serialized_user.errors, 422)
    
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise ValidationError('Passwords do not match')
            exp_date = datetime.now() + timedelta(days=1)
            token = jwt.encode(
                payload={
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'is_admin': user.is_staff
                    },
                    'exp' : int(exp_date.strftime('%s'))
                },
                key=settings.SECRET_KEY,
                algorithm='HS256'
            )
            return Response({ 'message': 'Login was successful', 'token': token })

        except (User.DoesNotExist, ValidationError) as e:
            print(e)
            raise NotAuthenticated('Invalid credentials')
        except Exception as e:
            print(e)
            return Response('Something went wrong', 500)

class UserProfileView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request):
        user = request.user
        serialized_user = UserSerializer(user, data=request.data, partial=True)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, 200)
        return Response(serialized_user.errors, 422)