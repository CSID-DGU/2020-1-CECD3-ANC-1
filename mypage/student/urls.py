from django.urls import path
from . import views

app_name='student'

urlpatterns=[
    path('<int:course_id>',views.student, name="studentMain"),
    path('<int:question_id>/',views.sdetail, name="sdetail"),
    path('post/questions/<int:course_id>',views.postQuestions,name="postQuestions"),
    path('ask/questions/<int:course_id>',views.askQuestion,name="askQuestion"),
    path('write/comment/<int:question_id>/',views.writeComment, name="writeComment"),
    path('like/<int:question_id>/<int:id>',views.like, name="like"),

]