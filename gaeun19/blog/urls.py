# 포스트 목록 페이지를 만들기 위해 만든 파이썬 파일

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('portfolio-details.html', views.portfolio),
    # path('',views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page)
]