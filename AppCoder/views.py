from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "AppCoder/index.html")

def chau(request):
    return render(request, "AppCoder/index.html")
