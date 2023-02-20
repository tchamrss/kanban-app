from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import Tasks

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(min_length=5, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username','email', 'password']
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'created_at','author','priority','due_date']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}} #extra_kwargs allows us to configure few extra settings in our Serializer,here making sure password is write only and more than 5 characters.

        