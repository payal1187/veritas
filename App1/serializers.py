from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class CustomerSerializer(serializers.ModelSerializer):
    #email =serializers.EmailField(required=True)
    #password = serializers.CharField(required=True)
    class Meta:
        model = Customer
        fields = ["name","surname","email","password","token"]


'''class CustomerChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    class Meta:
        model = Customer
        fields = ["old_password","password","password2"]


        def validate(self,data):
            password = data.get('password')
            password2 = data.get('password2')
            user = self.context.get('user')
            if password != password2:
                raise serializers.ValidationError({"password":"password fields didn't match"})
            user.set_password('password')
            user.save()
            return data
'''



class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = Subscription
        fields = ["name","email"]

class CatalogSubscriptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = Subscription
        fields = ["name","email"]
