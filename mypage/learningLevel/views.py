from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    inputId = request.POST.get('id', None)
    inputPassword = request.POST.get('pw', None)
    print(inputId)
    print(inputPassword)
    return redirect('learningLevel/')