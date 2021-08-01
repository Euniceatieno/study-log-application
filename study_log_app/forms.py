from django import forms
from django.forms import widgets
from .models import Topic,Entry

class TopicForm(forms.ModelForm): #Allowing users to add their own  topics.
    class Meta:
        model =Topic
        fields =['the_topic']
        labels = {'the_topic':''}
class EntryForm(forms.ModelForm):
    class Meta:
        model =Entry
        fields =['text']
        labels = {'text':'Entry:'}
        widgets ={'text':forms.Textarea (attrs= {'cols':80})}