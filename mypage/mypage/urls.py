"""mypage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import learningLevel.views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learningLevel/',include('learningLevel.urls')),
    path('answerQuestions/',include('answerQuestions.urls')),
    path('chatbot/', include('chatbot.urls')),
    url(r'^login$',learningLevel.views.login),
    url(r'^signin/',learningLevel.views.signin),
    url(r'^signout/',learningLevel.views.signout),
    url(r'^crawler/(?P<name>[-\w]+)', learningLevel.views.crawler2),
    url(r'^crawler/', learningLevel.views.crawler),
    url(r'^crawlAct$', learningLevel.views.crawlAct),
]
