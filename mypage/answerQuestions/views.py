from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *



def index2(request,course_id):
    if request.session.get('user',False):
        questLists=Question.objects.filter(q_c_id=course_id)
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4:
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            course = MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id)
            return render(request, 'index2.html', {'questLists':questLists,'teachList':teachList,'course':course})
        else:
            return render(request, 'index2.html', )
    else :
        return render(request, 'index2.html')

def detail(request, question_id):
    question=Question.objects.get(q_id=question_id)
    context={'question':question}
    if request.session.get('user', False):
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4:
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            return render(request, 'detailInfo.html', {'question':question,'teachList':teachList})
    else:
        return render(request,'detailInfo.html',context)

def answerCreate(request, question_id):
    question_answer=Question.objects.get(q_id=question_id)
    answer=request.POST['answer']
    question_answer.answer=answer
    question_answer.save()
    questLists=Question.objects.all()
    """return render(request, 'index2.html',{'questLists':questLists})"""
    return redirect('answerQuestions:detail',question_id=question_answer.q_id)

