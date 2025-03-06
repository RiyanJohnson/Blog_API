from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializer import PostSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def get_post(request):
    author = User.objects.all()
    posts = Post.objects.select_related('author').all()
    serializer = PostSerializer(posts, many = True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(author=request.user)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def post_detail(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CommentSerializer(data=request.data, context={"request": request, "post": post})
    serializer.is_valid(raise_exception=True)
    serializer.save(author=request.user, post=post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)