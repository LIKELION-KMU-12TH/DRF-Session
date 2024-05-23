<<<<<<< HEAD
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListAPIView.as_view()), # get - 블로그 리스트 조회
    path('<int:blog_id>/', views.BlogDetailAPIView.as_view()), # post - 블로그 작성
=======
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListAPIView.as_view()),
    path('<int:blog_id>/', views.BlogDetailAPIView.as_view()),
>>>>>>> 7b4a247334409ecc4f201fd6c81ff925389d25b6
]