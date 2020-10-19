from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *

def index2(request,course_id):
    if request.session.get('user',False):
        questLists=Question.objects.filter(q_c_id=course_id)
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        """if MdlRoleAssignments.objects.filter(userid=userid, roleid=4):"""

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

        print('mol', mol)
        print('molang', molang)


        #teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
        #course = MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id)
        course=MdlCourse.objects.get(id=course_id)
        return render(request, 'index2.html', {'questLists':questLists,'teachList':molang,'course':course})
        """else:
            return render(request, 'index2.html', )"""
    else :
        return render(request, 'signin.html')

def detail(request, question_id):
    question=Question.objects.get(q_id=question_id)
    context={'question':question}
    if request.session.get('user', False):
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        """if MdlRoleAssignments.objects.filter(userid=userid, roleid=4):"""
        #teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
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


        return render(request, 'detailInfo.html', {'question':question,'teachList':molang})
    else:
        return render(request,'signin.html',context)

def answerCreate(request, question_id):
    question_answer=Question.objects.get(q_id=question_id)
    answer=request.POST['answer']
    question_answer.answer=answer
    question_answer.save()
    questLists=Question.objects.all()
    """return render(request, 'index2.html',{'questLists':questLists})"""
    return redirect('answerQuestions:detail',question_id=question_answer.q_id)

