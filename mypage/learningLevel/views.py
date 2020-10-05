from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as dlogout
from .models import *
import bcrypt
from .crawler import eclass

# Create your views here.

def index(request):
    if request.session.get('user',False):
        enrolList = MdlEnrolFlatfile.objects.get(userid=request.session['user'])
        courseid = enrolList.courseid
        studentLists=MdlEnrolFlatfile.objects.exclude(userid=request.session['user']).filter(courseid=courseid)
        return render(request, 'index.html',{'students':studentLists})
    else:
        return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signout(request):
    request.session.clear()
    return render(request, 'index.html')

def login(request):
    inputId = request.POST.get('id', None)
    inputPassword = request.POST.get('pw', None)
    check = MdlUser.objects.filter(username=inputId)[0].password.replace('$2y$', '$2a$')
    if not MdlUser.objects.filter(username=inputId).exists():
        return render(request, 'signin.html')
    if not bcrypt.checkpw(inputPassword.encode('utf-8'), check):
        return render(request, 'signin.html')
    else:
        u = MdlUser.objects.filter(username=inputId)[0]
        if u != None:
            request.session['user'] = inputId
            return redirect('learningLevel/')

def crawler(request):
    return render(request, 'crawler.html')

def crawlAct(request):
    inputId = request.POST.get('id', None)
    inputPassword = request.POST.get('pw', None)
    inputCode = request.POST.get('code', None)
    df, name = eclass(inputId, inputPassword, inputCode)
    task=[] #과제
    try:
        hw_instance = HomeWork.objects.filter(code = inputCode).delete()
    except:
        pass
    for i in df:
        hw_instance = HomeWork(code = inputCode, name = name, title=i['title'], start = i['start'], end = i['end'])
        hw_instance.save()
        task.append({'title': i['title'], 'start': i['start'], 'end': i['end']})
    context = {'task': task, 'code': inputCode, 'name': name}
    return render(request, 'crawler.html', context)