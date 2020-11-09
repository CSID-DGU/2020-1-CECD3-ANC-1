from django.urls import path
from . import views

app_name='answerQuestions'

urlpatterns=[
    path('<int:course_id>',views.index2, name="mainpage"),
    path('<int:question_id>/<student_id>/<int:course_id>',views.detail, name="detail"),
    path('answer/create/<int:question_id>/<student_id>/<int:course_id>',views.answerCreate,name="answerCreate"),
    path('answer/create2/<int:question_id>/<student_id>/<int:course_id>',views.answerCreate2,name="answerCreate2"),
    path('incParticipation/<int:question_id>/<student_id>/<int:course_id>',views.incParticipation, name="incParticipation")

]