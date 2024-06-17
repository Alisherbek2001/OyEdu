from django.urls import path
from .views import *
urlpatterns = [
    path('category/',CategoryListCreateApiView.as_view(),name='category-list'),
    path('category/<int:pk>/',CategoryDetailApiView.as_view(),name='category-detail'),
    path('news/',NewsListCreateApiView.as_view(),name='news-list'),
    path('news/<int:pk>/',NewsDetailApiView.as_view(),name='news-detail'),
    path('blog/',BlogListCreateApiView.as_view(),name='blog-list'),
    path('blog/<int:pk>/',BlogDetailApiView.as_view(),name='blog-detail'),
    path('teacher/',TeacherListCreateApiView.as_view(),name='teacher-list'),
    path('teacher/<int:pk>/',TeacherDetailApiView.as_view(),name='teacher-detail'),
    path('course/',CourseListCreateApiView.as_view(),name='course-list'),
    path('course/<int:pk>/',CourseDetailApiView.as_view(),name='course-detail'),
    path('student/',StudentListCreateApiView.as_view(),name='student-list'),
    path('student/<int:pk>/',StudentDetailApiView.as_view(),name='student-detail'),
]