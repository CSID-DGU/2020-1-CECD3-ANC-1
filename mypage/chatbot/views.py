from django.shortcuts import render
from .models import *
# Create your views here.

def index3(request):
    """if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if ((MdlRoleAssignments.objects.get(userid=userid)).roleid) == 4 :
            teachList = MdlEnrolFlatfile.objects.filter(userid=userid)
            context = {'teachList':teachList}
            return render(request, 'chatbot/index3.html',context)
        else :
            return render(request, 'chatbot/index3.html')"""
    return render(request, 'chatbot/index3.html',)