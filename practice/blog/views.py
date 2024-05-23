from django.shortcuts import render, get_object_or_404
from .models import Blog
from .serializer import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BlogListAPIView(APIView):
    @swagger_auto_schema(
        operation_id='리스트 조회',
        operation_description='블로그 리스트 조회',
        tags=['ListCreate'],
        responses={200: BlogSerializer(many=True)}
    )
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_id='블로그글 생성',
        operation_description='블로그글 생성',
        tags=['ListCreate'],
        request_body=BlogSerializer,
        responses={201: BlogSerializer, 400: 'Error message'}
    )
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailAPIView(APIView):
    def get_object(self, blog_id):
        return get_object_or_404(Blog, id=blog_id)

    @swagger_auto_schema(
        operation_id='블로그 상세 조회',
        operation_description='블로그 글 상세 조회',
        tags=['DetailUpdateDelete'],
        responses={200: BlogSerializer}
    )
    def get(self, request, blog_id):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_id='블로그 수정',
        operation_description='블로그 글 수정',
        tags=['DetailUpdateDelete'],
        request_body=BlogSerializer,
        responses={200: BlogSerializer, 400: 'Error message'}
    )
    def put(self, request, blog_id):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id='블로그 삭제',
        operation_description='블로그 글 삭제',
        tags=['DetailUpdateDelete'],
        responses={204: 'No Content'}
    )
    def delete(self, request, blog_id):
        blog = self.get_object(blog_id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
