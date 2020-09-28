from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import MdlQuestion

def index2(request):
    questLists=MdlQuestion.objects.filter(id=1)
    return render(request, 'index2.html', {'questLists':questLists})