from rest_framework import serializers
from django.contrib.auth import get_user_model


User= get_user_model()

class registerUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email','password', 'mobile','gender', 'address','landmark','country','state','city','pincode')
        

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)