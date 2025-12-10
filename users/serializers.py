from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken

# Serializer for registering a new user
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

# Meta class to specify model and fields
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'role')

# Validate that the two passwords match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password don't match."})
        return attrs

# Method to create a new user
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            role = validated_data.get('role', 'customer')
        )

# Set the user's password
        user.set_password(validated_data['password'])
        user.save()
        return user