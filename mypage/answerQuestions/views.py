from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *

def index2(request):
    if request.session.get('user',False):
        enrolList=MdlEnrolFlatfile.objects.get(userid=request.session['user'])
        courseid=enrolList.courseid
        questLists=Question.objects.filter(q_c_id=courseid)
        return render(request, 'index2.html', {'questLists':questLists})
    else :
        return render(request, 'index2.html')

def detail(request, question_id):
    question=Question.objects.get(q_id=question_id)
    context={'question':question}
    return render(request,'detailInfo.html',context)

def answerCreate(request, question_id):
    question_answer=Question.objects.get(q_id=question_id)
    answer=request.POST['answer']
    question_answer.answer=answer
    question_answer.save()
    questLists=Question.objects.all()
    """return render(request, 'index2.html',{'questLists':questLists})"""
    return redirect('answerQuestions:detail',question_id=question_answer.q_id)


