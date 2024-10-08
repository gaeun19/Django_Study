from django.shortcuts import render
from . import views

# Create your views here.

def index(request):
    return render(request, 'index.html')  # templates 폴더 안의 index.html을 렌더링


def portfolio_details(request):
    return render(request, 'portfolio-details.html')  # 'portfolio-details.html' 템플릿을 렌더링
