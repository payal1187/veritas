from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name","surname","email","password","token"]


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True,required=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True,required=True)
    class Meta:
        model = Customer
        fields = ["password","password2"]

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm password doesn't match.")
        user.set_password(password)
        user.save()
        return data