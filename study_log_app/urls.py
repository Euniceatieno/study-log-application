from django.urls import path
from . import views

app_name = 'study_log_app'


urlpatterns=[
    #home
    path('',views.index,name='index'), #2nd argument to specify which function to call
                                      #3rd argument ,the name to use whenever we want to provide a link to the home page
    #topics page 
    path('topics/',views.topics,name='topics'),

    #single topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #adding topics page
    path('new_topic/',views.new_topic,name='new_topic'),

    #edit_topic
    path('edit_topic/<int:topic_id>/',views.edit_topic,name='edit_topic'),
     
    #adding new entry page
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),

    #edit entry
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),

]