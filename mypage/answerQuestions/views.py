from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Question

def index2(request):
    questLists=Question.objects.all()
    return render(request, 'index2.html', {'questLists':questLists})

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


