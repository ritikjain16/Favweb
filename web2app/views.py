from django.shortcuts import render

from .models import MovieModel
# Create your views here.

def home(request):
    movie123 = MovieModel.objects.all()
    return render(request,'web2app/home.html',{'movie123':movie123})

def about(request):
    return render(request,'web2app/about.html')