from rest_framework import serializers,status
from .models import CustomUserManager,User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.response import Response

#register serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        #this are the fields that will be used for user registration
        fields = ('first_name', 'last_name', 'staff_id','phone_number','email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user( email=validated_data['email'],first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],staff_id=validated_data['staff_id'],phone_number=validated_data['phone_number'],
        password=validated_data['password'])
        return user

#login serializer for user login
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True,style={'input_type': 'password'})

    def validate(self, data):
        email= data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.', code='authorization')
            else:
                data['user'] = user
                return data
        return Response({'error': 'invalid Password.'}, status=status.HTTP_400_BAD_REQUEST)
    

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, data):
        try:
            user = User.objects.get(email=data)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return data

# To verify the password reset token and set a new password, you can create another serializer. Here's an example:
class PasswordVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password,
        )
        if not user:
            raise serializers.ValidationError(
                'Unable to log in with provided credentials.',
                code='authorization',
            )
        data['user'] = user
        return data

# To confirm password reset
class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if new_password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        return data

