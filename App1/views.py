import logging
import random
import string
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from .models import *
from .serializers import *

class SignUp(APIView):
    """SignUp
    this api is responsible to register new user
    Body:
        {
            "first_name": str,
            "last_name": str,
            "email": str,
            "password": str
        }
    """

    def post(self, request):
        data = request.data
        data['password'] = make_password(data['password'])  # hash the password
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logging.info("save success")
            return Response(
                data={
                    "IsStatus": True,
                    "Data": serializer.data,
                    "Message": "User created successfully",
                },
                status=status.HTTP_201_CREATED,
            )

class SignIn(APIView):
    """SignIn
    this api is responsible for signin to user
    body:
        {
            "email": str,
            "password": str
        }
    """

    def post(self, request):

        data = request.data
        email = data.get("email",None)
        password = data.get("password",None)

        if email and password:
            user_profile = Customer.objects.get(email=email)
            #user_pass = Customer.objects.get(password=password)
            #password = make_password(password)  # hash the password
            print(password,"####",check_password(user_profile.password,password),user_profile.password)
            if user_profile.is_active and check_password(password,user_profile.password):
                #login(request, user_profile)
                refresh = RefreshToken.for_user(user_profile)
                user_profile.token = str(refresh.access_token)
                #user_profile.save()  # save the token to the database
                serializer = CustomerSerializer(user_profile)
                logging.info("Sign in success")
                return Response(
                        data={
                            "IsStatus": True,
                            "Data": serializer.data,
                            "Message": "SignIn Successfully",
                        },
                        status=status.HTTP_200_OK,
                    )
            else:
                    return Response(
                        data={
                            "IsStatus": False,
                            "Message": "Provided email and password is mismatch.",
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

        else:
                return Response(
                    data={"IsStatus": False, "Message": "Provide email and password."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        #except Exception as e:
    logging.error("sign in failed because : " )
            #return Response(data={"IsStatus": False, "Message": "Invalid email or password."},status=status.HTTP_400_BAD_REQUEST,)



class ChangePassword(APIView):
    permission_classes = IsAuthenticated
    def get_object(self,queryset=None):
        return self.request.user






class Newsletter_Subscription(APIView):
    def post(self,request):
        data = request.data
        serializers = NewsletterSubscriptionSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            return Response({"msg":"Subscription for newsletter"})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class Catalog_Subscription(APIView):
    def post(self,request):
        data = request.data
        serializers = CatalogSubscriptionSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            return Response({"msg":"Subscription for catalog"})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
























