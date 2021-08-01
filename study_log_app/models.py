
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    the_topic=models.CharField(max_length=200)
    input_date=models.DateTimeField(auto_now_add=True) #auto now add automatically sets the attribute 
                                                      #to the current date and time. 


    owner=models.ForeignKey(User,on_delete=models.CASCADE) #when a user is deleted all the topics associated with it are also deleted
    def __str__(self):
        return self.the_topic #displays a simple rep of the model

class Entry(models.Model):
    topic= models.ForeignKey(Topic,on_delete=models.CASCADE) #when a topic is deleted,the enteries associated with it are also deleted
    text=models.TextField()
    input_date=models.DateTimeField(auto_now_add=True) 

    class Meta: 
        verbose_name_plural='entries'     

    def __str__(self):
        return f"{self.text[:50]}..."