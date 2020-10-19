from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *



def student(request,course_id):
    if request.session.get('user',False):
        questLists=Question.objects.filter(q_c_id=course_id)
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=5):
            #enrolList = MdlEnrolFlatfile.objects.filter(userid=userid)
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
            #course = MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id)
            course = (MdlCourse.objects.get(id=course_id))
            return render(request, 'studentIndex.html', {'questLists':questLists,'enrolList':molang,'course':course})
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
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=5):
            #teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
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
            commentList=SComment.objects.filter(q_id=question_id)
            answerNo=SComment.objects.filter(q_id=question_id).count()
            return render(request, 'sdetailInfo.html', {'question':question,'teachList':molang,
                                                        'commentList':commentList,'answerNo':answerNo,})
    else:
        return render(request,'sdetailInfo.html',context)

def postQuestions(request, course_id):
    if request.session.get('user',False):
        questLists=Question.objects.filter(q_c_id=course_id)
        user = (MdlUser.objects.get(username=request.session.get('user', False)))
        userid = user.id
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=5):
            #enrolList = MdlEnrolFlatfile.objects.filter(userid=userid)
            #course = MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id)
            #course_name= MdlEnrolFlatfile.objects.get(userid=userid, courseid=course_id).coursename

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
            course=(MdlCourse.objects.get(id=course_id))

            return render(request, 'postQuestions.html', {'enrolList':molang,'course':course,})
        else :
            return render(request,'postQuestions.html')
    return render(request, 'postQuestions.html')

def askQuestion(request, course_id):

    #course_name=(MdlEnrolFlatfile.objects.get(courseid=course_id,roleid=4)).coursename
    """start"""
    course_name=(MdlCourse.objects.get(id=course_id)).fullname

    """end"""

    username=request.session.get('user')
    question=request.POST['question']
    year=request.POST.get('year')
    semester=request.POST.get('semester')
    chapter=request.POST.get('chapter')
    new_questions=Question.objects.create(q_s_id=username,question=question,q_c_id=course_id,
                                          t_year=year, t_semester=semester,ch_id=chapter,q_c_name=course_name)


    return redirect('student:studentMain', course_id=course_id)

def writeComment(request, question_id):
    question_id=question_id
    username=request.session.get('user')
    answer=request.POST['studentA']
    new_comment=SComment.objects.create(userid=username, q_id=question_id, answer=answer)

    return redirect('student:sdetail', question_id=question_id)


def like(request, question_id, id):

    comment = SComment.objects.get(q_id=question_id, id=id)
    like=SComment.objects.get(q_id=question_id, id=id).like
    if comment.like:
        like = like + 1
    else:
        like=1
    comment.like=like
    comment.save()

    return redirect('student:sdetail', question_id=question_id, )
