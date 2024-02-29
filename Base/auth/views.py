from Base.models import Client
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import ClientRegister,ClientSerializer
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializer import CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed as e:
            return Response({
                'status': False,
                'message': "Incorrect username or password"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def ClientRegisters(request):
    data = request.data
    serializer = ClientRegister(data=data,many=False)
    if serializer.is_valid():
        if User.objects.filter(username=data['home_number']).exists():
            return Response({'Error' : 'Account Already Existed'},status=status.HTTP_400_BAD_REQUEST)
        else : 
            user = User.objects.create(
                username = data['home_number'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = make_password(data['password'])
            )
            group = Group.objects.get(name="client")
            user.groups.add(group)
            Client.objects.create(user=user,adress=data['adress'],Home_number=data['home_number'],phone_number=data['phone_number'])
            return Response({"Detail":"Account Created Succesfully"},status=status.HTTP_201_CREATED)
    else:
        return Response({serializer.errors})
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Get_Profile(request):
    user = User.objects.get(username=request.user)
    if user.groups.filter(name="client").exists():
        data = Client.objects.get(user=user)
        serializer = ClientSerializer(data,many=False)
        return Response({"Info":serializer.data})
    return Response({"Ret","Re"})


@api_view(['POST'])
def logout(request):
    if 'refresh_token' in request.data:
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid or missing refresh token."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)