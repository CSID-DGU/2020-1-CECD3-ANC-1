from django.urls import path
from . import views

app_name='learningLevel'

urlpatterns=[
    path('',views.index,name="main"),
    path('<int:course_id>/',views.learningLevelDetail, name="learningLevelDetail"),
]