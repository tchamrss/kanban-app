from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tasks

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username','email']
    

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'created_at','author','priority','due_date']