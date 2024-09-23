from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer): #convert to json format
    class Meta:
        model = Books
        fields = '__all__'
class Register_serializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)  # hide password
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','password','email']

    def create(self,validated_data): # after validation validated data (deserialized data ) is sent to create() function
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        return user