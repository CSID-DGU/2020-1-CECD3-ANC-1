from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as dlogout
from .models import *
import bcrypt
from .crawler import eclass
from plotly.offline import plot
from plotly.graph_objs import Scatter, Layout, Figure
import json

# Create your views here.

def index(request):
    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        temp=MdlRoleAssignments.objects.filter(userid=userid)
        print('temp',temp)
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=4):
            enrolList=[]
            for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
                enrolList.append(i)
            print(enrolList)
            enrolid=MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')
            print('enrolid',enrolid)

            courseList=[]
            cnt = 0
            for i in range(0,len(enrolList)):
                courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))

            #int('결과',courseList)
            #print((courseList[0][0])[0])
            #print((courseList[1][0])[0])
            fullname=[]

            courseIdList=[]

            for i in range(0,len(courseList)):
                courseIdList.append((courseList[i][0])[0])
            print('courseIdList',courseIdList)

            cnt=0
            mol=[]

            for i in range(0,len(courseList)):
                if MdlCourse.objects.filter(id=courseIdList[i]) and cnt ==0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
                elif MdlCourse.objects.filter(id=courseIdList[i]) and cnt !=0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
            molang=MdlCourse.objects.filter(id=100000)
            for i in range(0,len(courseList)):
                molang=molang|mol[i]

            print('mol',mol)
            print('molang',molang)

            return render(request, 'index.html',{'courses':molang})
        elif MdlRoleAssignments.objects.filter(userid=userid, roleid=5):
            enrolList = []
            for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
                enrolList.append(i)
            print(enrolList)
            enrolid = MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')
            print('enrolid', enrolid)

            courseList = []
            cnt = 0
            for i in range(0, len(enrolList)):
                courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))

            print('courseList', list(courseList))

            print('결과', courseList)
            print((courseList[0][0])[0])
            print((courseList[1][0])[0])
            fullname = []

            courseIdList = []

            for i in range(0, len(courseList)):
                courseIdList.append((courseList[i][0])[0])
            print('courseIdList', courseIdList)

            cnt = 0
            mol = []

            for i in range(0, len(courseList)):
                if MdlCourse.objects.filter(id=courseIdList[i]) and cnt == 0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
                elif MdlCourse.objects.filter(id=courseIdList[i]) and cnt != 0:
                    mol.appen(MdlCourse.objects.filter(id=courseIdList[i]))
            molang = MdlCourse.objects.filter(id=100000)
            for i in range(0, len(courseList)):
                molang = molang | mol[i]

            print('mol', mol)
            print('molang', molang)

            return render(request, 'student.html',{'enrolList':molang})
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'signin.html')


def signin(request):
    return render(request, 'signin.html')

def signout(request):
    request.session.clear()
    return render(request, 'signin.html')

def login(request):
    inputId = request.POST.get('id', None)
    inputPassword = request.POST.get('pw', None)
    if not MdlUser.objects.filter(username=inputId).exists():
        context = {'error':"아이디나 비밀번호가 일치하지 않습니다"}
        return render(request, 'signin.html', context)
    else:
        check = MdlUser.objects.filter(username=inputId)[0].password.replace('$2y$', '$2a$')
        if not bcrypt.checkpw(inputPassword.encode('utf-8'), check):
            context = {'error':"아이디나 비밀번호가 일치하지 않습니다"}
            return render(request, 'signin.html', context)
        else:
            u = MdlUser.objects.filter(username=inputId)[0]
            if u != None:
                request.session['user'] = inputId
                return redirect('learningLevel/')

def crawler2(request, name):
    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=4) :


            """start"""
            enrolList = []
            for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
                enrolList.append(i)
            print(enrolList)
            enrolid = MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')
            print('enrolid', enrolid)

            courseList = []
            cnt = 0
            for i in range(0, len(enrolList)):
                courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))

            # int('결과',courseList)
            # print((courseList[0][0])[0])
            # print((courseList[1][0])[0])
            fullname = []

            courseIdList = []

            for i in range(0, len(courseList)):
                courseIdList.append((courseList[i][0])[0])
            print('courseIdList', courseIdList)

            cnt = 0
            mol = []

            for i in range(0, len(courseList)):
                if MdlCourse.objects.filter(id=courseIdList[i]) and cnt == 0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
                elif MdlCourse.objects.filter(id=courseIdList[i]) and cnt != 0:
                    mol.appen(MdlCourse.objects.filter(id=courseIdList[i]))
            molang = MdlCourse.objects.filter(id=100000)
            for i in range(0, len(courseList)):
                molang = molang | mol[i]


            """end"""




            if request.method == 'GET':
                item = HomeWork.objects.filter(name=name)
                hwList = []
                for i in item:
                    hwList.append({'title': i.title, 'start': i.start, 'end': i.end})
            return render(request, 'crawler.html', {'teachList':molang, 'task': hwList ,'name':name})
        else:
            return render(request, 'crawler.html')
    else:
        return render(request, 'signin.html')

def crawler(request):
    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=4) :

            """start"""
            enrolList = []
            for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
                enrolList.append(i)
            print(enrolList)
            enrolid = MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')
            print('enrolid', enrolid)

            courseList = []
            cnt = 0
            for i in range(0, len(enrolList)):
                courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))

            # int('결과',courseList)
            # print((courseList[0][0])[0])
            # print((courseList[1][0])[0])
            fullname = []

            courseIdList = []

            for i in range(0, len(courseList)):
                courseIdList.append((courseList[i][0])[0])
            print('courseIdList', courseIdList)

            cnt = 0
            mol = []

            for i in range(0, len(courseList)):
                if MdlCourse.objects.filter(id=courseIdList[i]) and cnt == 0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
                elif MdlCourse.objects.filter(id=courseIdList[i]) and cnt != 0:
                    mol.appen(MdlCourse.objects.filter(id=courseIdList[i]))
            molang = MdlCourse.objects.filter(id=100000)
            for i in range(0, len(courseList)):
                molang = molang | mol[i]


            """end"""

            return render(request, 'crawler.html', {'teachList':molang})
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
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=4) :

            """start"""
            enrolList = []
            for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
                enrolList.append(i)
            print(enrolList)
            enrolid = MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')
            print('enrolid', enrolid)

            courseList = []
            cnt = 0
            for i in range(0, len(enrolList)):
                courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))

            # int('결과',courseList)
            # print((courseList[0][0])[0])
            # print((courseList[1][0])[0])
            fullname = []

            courseIdList = []

            for i in range(0, len(courseList)):
                courseIdList.append((courseList[i][0])[0])
            print('courseIdList', courseIdList)

            cnt = 0
            mol = []

            for i in range(0, len(courseList)):
                if MdlCourse.objects.filter(id=courseIdList[i]) and cnt == 0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
                elif MdlCourse.objects.filter(id=courseIdList[i]) and cnt != 0:
                    mol.appen(MdlCourse.objects.filter(id=courseIdList[i]))
            molang = MdlCourse.objects.filter(id=100000)
            for i in range(0, len(courseList)):
                molang = molang | mol[i]


            """end"""



            context = {'task': task, 'name': inputName, 'update': 1, 'teachList':molang}
            return render(request, 'crawler.html', context)
        else:
            context = {'task': task, 'name': inputName, 'update': 1}
            return render(request, 'crawler.html', context)
    else:
        return render(request, 'signin.html')

def learningLevelDetail(request,course_id):


    enrolid=(MdlEnrol.objects.get(courseid=course_id,enrol='manual')).id
    students=MdlUserEnrolments.objects.filter(enrolid=enrolid)
    enrolPeople=[]

    """start"""
    for i in MdlUserEnrolments.objects.filter(enrolid=enrolid).values_list('userid'):
        enrolPeople.append(i)
    print('enrolPeople', enrolPeople)
    studentList=[]

    for i in range(0, len(enrolPeople)):
        if ((MdlRoleAssignments.objects.filter(userid=enrolPeople[i][0],roleid=5)).values_list('userid')):
            studentList.append(enrolPeople[i][0])

    cnt = 0
    mol2 = []
    print('studentList',studentList)

    for i in range(0, len(studentList)):
        if MdlUserEnrolments.objects.filter(userid=studentList[i],enrolid=enrolid) and cnt == 0:
            mol2.append(MdlUserEnrolments.objects.filter(userid=studentList[i],enrolid=enrolid))
        #elif MdlUserEnrolments.objects.filter(userid=studentList[i]) and cnt != 0:
            #mol2.append(MdlUserEnrolments.objects.filter(userid=studentList[i]))
    molang2 = MdlUserEnrolments.objects.filter(id=10000)

    print('mol2',mol2)
    for i in range(0, len(studentList)):
        molang2 = molang2 | mol2[i]

    """end"""
    #for i in range(0, len(enrolPeople)):
        #studentList.append(MdlRoleAssignments.objects.filter(id=enrolPeople[i][0]).values_list(''))



    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=4) :

            teachList=MdlCourse.objects.filter(id=course_id)

            x_data = ['A', 'B', 'C', 'D']
            #y_data = [1, 2, 1, 0]
            y_data=[]

            A=(MdlUserEnrolments.objects.filter(enrolid=enrolid,grade__gte=50)).count()
            y_data.append(A)
            B=(MdlUserEnrolments.objects.filter(enrolid=enrolid,grade__gte=40,grade__lte=49)).count()
            y_data.append(B)
            C = (MdlUserEnrolments.objects.filter(enrolid=enrolid,grade__gte=30, grade__lte=40)).count()
            y_data.append(C)
            D = (MdlUserEnrolments.objects.filter(enrolid=enrolid,grade__lte=20)).count()
            D=D-1
            y_data.append(D)

            plot_div = plot([Scatter(x=x_data, y=y_data,
                                     mode='lines',
                                     opacity=0.8, marker_color='blue',fillcolor='rgba(0,0,0,0)')],
                            output_type='div')
            course=MdlCourse.objects.get(id=course_id)

            enrolList = []
            for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
                enrolList.append(i)
            print(enrolList)
            enrolid = MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')
            print('enrolid', enrolid)

            courseList = []
            cnt = 0
            for i in range(0, len(enrolList)):
                courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))

            # int('결과',courseList)
            # print((courseList[0][0])[0])
            # print((courseList[1][0])[0])
            fullname = []

            courseIdList = []

            for i in range(0, len(courseList)):
                courseIdList.append((courseList[i][0])[0])
            print('courseIdList', courseIdList)

            cnt = 0
            mol = []

            for i in range(0, len(courseList)):
                if MdlCourse.objects.filter(id=courseIdList[i]) and cnt == 0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
                elif MdlCourse.objects.filter(id=courseIdList[i]) and cnt != 0:
                    mol.append(MdlCourse.objects.filter(id=courseIdList[i]))
            molang = MdlCourse.objects.filter(id=100000)
            for i in range(0, len(courseList)):
                molang = molang | mol[i]

            print('mol', mol)
            print('molang', molang)


            context = {'students': molang2, 'teachList':molang,'plot_div':plot_div,'course':course,
                       'x_data':x_data,'y_data':y_data}


            return render(request, 'learningLevelDetail.html',context)
        else :

            context={'students': students}
            return render(request, 'learningLevelDetail.html',context)


    #return render(request, 'index.html',context)
