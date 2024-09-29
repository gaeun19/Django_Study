from django.shortcuts import render

# Create your views here.

#
def main(request):
    return render(request, 'index.html')

def pf_detail(request):
    return render(request,'portfolio-details.html')