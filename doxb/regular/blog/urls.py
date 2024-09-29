from django.urls import path
from . import views

# 앞으로 현재 프로젝트 내에서 blog/ 안에 있는 경로는 모두 blog_app
app_name= 'blog_app'  # blog_app:blog  -> localhost:8000/blog/post-list
# url 'blog_app:about_me'  localhost:8000/blog/about-me

urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    # name= 개발자가 이 주소를 부를 이름
    path('', views.main, name='main'), # localhost:8000/blog 경로, 경로를 호출하면 실행할 함수의 위치
    path('portfolio-details.html', views.pf_detail, name='pf_detail')
]
