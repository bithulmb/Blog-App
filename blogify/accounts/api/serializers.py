from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
