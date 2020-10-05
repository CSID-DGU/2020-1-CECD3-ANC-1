from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as dlogout
from .models import *
import bcrypt
from .crawler import eclass

# Create your views here.

def index(request):

    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4 :
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            #courseid = teachList.courseid
            #studentLists=MdlEnrolFlatfile.objects.filter(courseid=courseid,roleid=5)
            return render(request, 'index.html', {'teachList':teachList})
        else :
            return render(request, 'index.html')
    else  :
        return render(request, 'signin.html')


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

def crawler2(request, name):
    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4 :
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            #courseid = teachList.courseid
            #studentLists=MdlEnrolFlatfile.objects.filter(courseid=courseid,roleid=5)
            if request.method == 'GET':
                item = HomeWork.objects.filter(name=name)
                hwList = []
                for i in item:
                    hwList.append({'title': i.title, 'start': i.start, 'end': i.end})
            return render(request, 'crawler.html', {'teachList':teachList, 'task': hwList ,'name':name})
        else:
            return render(request, 'crawler.html')
    else:
        return render(request, 'signin.html')

def crawler(request):
    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4 :
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            #courseid = teachList.courseid
            #studentLists=MdlEnrolFlatfile.objects.filter(courseid=courseid,roleid=5)
            return render(request, 'crawler.html', {'teachList':teachList})
        else:
            return render(request, 'crawler.html')
    else:
        return render(request, 'signin.html')

def crawlAct(request):
    if request.session.get('user',False) :
        inputId = request.POST.get('id', None)
        inputPassword = request.POST.get('pw', None)
        inputName = request.POST.get('name', None)
        df= eclass(inputId, inputPassword, inputName)
        task=[] #과제
        try:
            hw_instance = HomeWork.objects.filter(name = inputName).delete()
        except:
            pass
        for i in df:
            hw_instance = HomeWork(name = inputName, title=i['title'], start = i['start'], end = i['end'])
            hw_instance.save()
            task.append({'title': i['title'], 'start': i['start'], 'end': i['end']})
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4 :
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            context = {'task': task, 'name': inputName, 'update': 1, 'teachList':teachList}
            return render(request, 'crawler.html', context)
        else:
            context = {'task': task, 'name': inputName, 'update': 1}
            return render(request, 'crawler.html', context)
    else:
        return render(request, 'signin.html')

def learningLevelDetail(request,course_id):
    students=MdlEnrolFlatfile.objects.filter(courseid=course_id, roleid=5)

    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4 :
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            context = {'students': students, 'teachList':teachList}
            return render(request, 'learningLevelDetail.html',context)
        else :
            context={'students': students}
            return render(request, 'learningLevelDetail.html',context)


    #return render(request, 'index.html',context)
