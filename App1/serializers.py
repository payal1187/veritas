from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class CustomerSerializer(serializers.ModelSerializer):
    #email =serializers.EmailField(required=True)
    #password = serializers.CharField(required=True)
    class Meta:
        model = Customer
        fields = ["name","surname","email","password","token"]


class CustomerChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    class Meta:
        model = Customer
        fields = ["old_password","password","password2"]

        def validate(self,data):
            if data['password'] != data['password2']:
                raise serializers.ValidationError({"password":"password fields didn't match"})
            return data




class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = Customer
        fields = ["name","email","is_subscribed_to_newsletter"]

class CatalogSubscriptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = Customer
        fields = ["name","email","is_subscribed_to_catalog"]
