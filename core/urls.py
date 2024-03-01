"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import statistics
from django.contrib import admin
from django.urls import path
from Home.views import *
from core import settings
from vege.views import *
from core.settings import *
from Home import views


urlpatterns = [
    path('', home),
    path('success_page/', success_page),
    path('admin/', admin.site.urls),
    path('receipe/', receipe,name="receipe"),
    path('about/', about,name="about"),
    path('contact/', contact,name="contact"),
    path('receipe_delete/<id>/',receipe_delete,name="receipe_delete"),
    path('update_receipe/<id>/',update_receipe,name="update_receipe"),
    path('login/', login_page,name="login_page"),
    path('register/', register_page,name="register_page"),
    path('receipe/', receipe,name="receipe"),
    path('students/', get_students,name="students"),
    path('students/', get_students,name="students"),
    path('send_email/', views.send_email,name='send_email'),
    path('see_marks/<student_id>/', see_marks , name="see_marks"),
]


