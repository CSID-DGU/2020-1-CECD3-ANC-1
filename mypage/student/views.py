from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *



def student(request,course_id):
    if request.session.get('user',False):
        questLists=Question.objects.filter(q_c_id=course_id)
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 5:
            enrolList = MdlEnrolFlatfile.objects.filter(userid=userid)
            course = MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id)
            return render(request, 'studentIndex.html', {'questLists':questLists,'enrolList':enrolList,'course':course})
        else:
            return render(request, 'studentIndex.html', )
    else :
        return render(request, 'studentIndex.html')

def sdetail(request, question_id):
    question=Question.objects.get(q_id=question_id)
    context={'question':question}
    if request.session.get('user', False):
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 5:
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            return render(request, 'sdetailInfo.html', {'question':question,'teachList':teachList})
    else:
        return render(request,'sdetailInfo.html',context)

def postQuestions(request, course_id):
    if request.session.get('user',False):
        questLists=Question.objects.filter(q_c_id=course_id)
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 5:
            enrolList = MdlEnrolFlatfile.objects.filter(userid=userid)
            course = MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id)
            course_name= MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id).coursename
            return render(request, 'postQuestions.html', {'enrolList':enrolList,'course':course,})
        else :
            return render(request,'postQuestions.html')
    return render(request, 'postQuestions.html')

def askQuestion(request, course_id):

    course_name=(MdlEnrolFlatfile.objects.get(courseid=course_id,roleid=4)).coursename
    username=request.session.get('user')
    question=request.POST['question']
    year=request.POST['year']
    semester=request.POST['semester']
    chapter=request.POST['chapter']
    new_questions=Question.objects.create(q_s_id=username,question=question,q_c_id=course_id,
                                          t_year=year, t_semester=semester,ch_id=chapter,q_c_name=course_name)


    return redirect('student:studentMain', course_id=course_id)

