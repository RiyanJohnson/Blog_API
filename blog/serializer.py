from rest_framework import serializers  
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id','title','content','date_posted','author']