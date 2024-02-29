from rest_framework import serializers
from Base.models import Client
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Client
        fields = ['user', 'adress','phone_number','Home_number']

class ClientRegister(serializers.ModelSerializer):
    adress = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    home_number = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','adress','phone_number','home_number']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # You can add custom claims to the token here if needed
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user is None:
            raise AuthenticationFailed("Incorrect username or password")

        # Assuming your user model has 'first_name' and 'last_name' fields
        refresh = self.get_token(user)
        data.pop('refresh', None)
        data.pop('access', None)
        data['user'] = {
            'id': user.id,
            'first_name': user.first_name,  # Corrected field name to 'first_name'
            'last_name': user.last_name,    # Corrected field name to 'last_name'
            'username': user.username,
            'email': user.email,
            'token': str(refresh.access_token)
        }
        data['status'] = True
        return data