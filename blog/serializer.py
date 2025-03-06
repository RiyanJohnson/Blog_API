from rest_framework import serializers  
from .models import Post, Comments
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    
    class Meta:
        model = Comments
        fields = ['id','text','date_posted','author']
        read_only_fields = ['id','post','date_posted','author']

        def create(self, validated_data):
            validated_data['author'] = self.context['request'].user
            validated_data['post'] = self.context['post']
            return super().create(validated_data)
        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comment = CommentSerializer(many = True, read_only = True)
    
    class Meta:
        model = Post
        fields = ['id','title','content','date_posted','author','comment']