from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_post(request):
    query_set = Blog.objects.all()
    serializer = BlogSerializer(query_set,many=True)
    return Response({'all_blogs': serializer.data})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_post(request):
    data = request.data
    data['creation_user'] = request.user.first_name + " " + request.user.last_name
    #return Response({'Errors': "erros"})
    serializer = BlogSerializer(data = data)
    if serializer.is_valid():
        all_post = Blog.objects.create(**data)
        response = BlogSerializer(all_post,many=False)
        return Response({'allPost': response.data})
    else:
        return Response({'Errors': serializer.errors})
@api_view(['PUT'])
@permission_classes([IsAuthenticated])    
def update_post(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    if not request.data :
        return Response({'Errors':"You can't be update post due passing parameters failed"},status=status.HTTP_403_FORBIDDEN)
    blog.name= request.data.get('title')
    blog.content= request.data.get('content')
    blog.save()
    serializer = BlogSerializer(blog,many=False)
    return Response({'postDetails': serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    if blog.creation_user != request.user.first_name +" "+ request.user.last_name :
        return Response({'Errors':"You can't be deleted post"},status=status.HTTP_403_FORBIDDEN)
    blog.delete()
    return Response({'details':'Products deleted successfully..!'},status= status.HTTP_200_OK)
