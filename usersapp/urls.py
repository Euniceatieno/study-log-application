
from django.urls import path, include #include imports default authentication  url patterns such login and logout
from . import views


app_name='usersapp'

urlpatterns=[
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register')

]