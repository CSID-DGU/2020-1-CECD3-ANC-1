from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from student.models import SComment
from .create_intent import create_intent
from .create_intent import update_intent

def index2(request,course_id):
    if request.session.get('user',False):
        questLists=Question.objects.filter(q_c_id=course_id)
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        enrolList = []
        for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
            enrolList.append(i)
        enrolid = MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')

        courseList = []
        cnt = 0
        for i in range(0, len(enrolList)):
            courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))
        fullname = []

        courseIdList = []

        for i in range(0, len(courseList)):
            courseIdList.append((courseList[i][0])[0])

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
        enrolList = []
        for i in MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid'):
            enrolList.append(i)
        enrolid = MdlUserEnrolments.objects.filter(userid=userid).values_list('enrolid')
        courseList = []
        cnt = 0
        for i in range(0, len(enrolList)):
            courseList.append(MdlEnrol.objects.filter(id=enrolList[i][0]).values_list('courseid'))
        fullname = []
        courseIdList = []

        for i in range(0, len(courseList)):
            courseIdList.append((courseList[i][0])[0])
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
        commentList=SComment.objects.filter(q_id=question_id)
        answerNo=SComment.objects.filter(q_id=question_id).count()
        return render(request, 'detailInfo.html', {'question':question,'teachList':molang, 'commentList':commentList, 'answerNo':answerNo})
    else:
        return render(request,'signin.html',context)

def answerCreate(request, question_id):
    question_answer=Question.objects.get(q_id=question_id)
    answer=request.POST['answer']
    question_answer.answer=answer
    question_answer.save()
    questLists=Question.objects.all()
    create_intent(question_answer.question, answer, question_answer.q_id)
    return redirect('answerQuestions:detail',question_id=question_answer.q_id)


def answerCreate2(request, question_id):
    question_answer=Question.objects.get(q_id=question_id)
    answer2=request.POST['answer2']
    question_answer.answer=answer2
    question_answer.save()
    questLists=Question.objects.all()
    update_intent(question_answer.question, answer2, question_answer.q_id)
    return redirect('answerQuestions:detail',question_id=question_answer.q_id)
