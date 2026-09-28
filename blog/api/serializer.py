from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    user = serializers.CharField(source = 'user.username')
    
    class Meta:
        model=Blog
        fields = ['id', 'title', 'user', 'content']
        
class BlogCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'user', 'content'
        ]
        read_only_fields=['user']
