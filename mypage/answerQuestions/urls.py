from django.urls import path
from . import views

app_name='answerQuestions'

urlpatterns=[
    path('<int:course_id>',views.index2, name="mainpage"),
    path('<int:question_id>/',views.detail, name="detail"),
    path('answer/create/<int:question_id>',views.answerCreate,name="answerCreate"),

]