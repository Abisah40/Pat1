# from .models import Usermanager
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password','first_name','last_name']
        extra_kwargs = {'password':{'write_only':True}}


    def create(self,validated_data):
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
    

            
        # def validate(self, attrs):
        #     data = super().validate(attrs)


        #     data['user'] = {
        #         'id': self.user.id,
        #         'email': self.user.email,
        #         'password': self.user.password,
        #         'username':self.user.username
        #     }

        #     return data
