from django.shortcuts import render
from learningLevel.models import *
# Create your views here.

def index3(request):
    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4 :
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            #courseid = teachList.courseid
            #studentLists=MdlEnrolFlatfile.objects.filter(courseid=courseid,roleid=5)
            return render(request, 'chatbot/index3.html', {'teachList':teachList})
        else :
            return render(request, 'chatbot/index3.html')
    else  :
        return render(request, 'chatbot/index3.html')