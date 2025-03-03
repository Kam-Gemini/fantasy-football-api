from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation, hashers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # Make password optional
    password_confirmation = serializers.CharField(write_only=True, required=False)  # Make password_confirmation optional

    def validate(self, data):
        # Only validate password if it's being updated
        if 'password' in data:
            password = data.pop('password')
            password_confirmation = data.pop('password_confirmation', None)  # Use .pop() with a default to avoid KeyError
            if password != password_confirmation:
                raise serializers.ValidationError({'password': 'Passwords do not match'})
            password_validation.validate_password(password)
            data['password'] = hashers.make_password(password)
        return data

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'is_staff', 'password', 'password_confirmation', 'favourite_team')