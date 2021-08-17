from django.shortcuts import render ,redirect #to redirect the user to the topics page once they have added their topic
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def index(request):
    return render(request,'study_log_app/index.html')
    
@login_required
def topics(request):
    topics=Topic.objects.filter(owner=request.user).order_by('input_date')#tells django to retrieve info whose owner attributes matches the current user.
    context={'topics':topics}
    return render(request,'study_log_app/topics.html',context)   


@login_required
def topic(request,topic_id):
    # topic=Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404
    
    entries=topic.entry_set.order_by('-input_date')
    context={'topic':topic,'entries':entries}
    return render(request,'study_log_app/topic.html',context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form =TopicForm()
    else: 
        #posting the data submitted
        form =TopicForm(request.POST,request.FILES)
        if form.is_valid(): #validating that all fields are filled in correctly
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save() #writes data to the database if the else condition is met
            return redirect('study_log_app:topics')
    context={'form':form}        
    return render(request,'study_log_app/new_topic.html', context)

@login_required
def edit_topic(request,topic_id):
        topic=Topic.objects.get(id=topic_id)
        if request.method!='POST':
            form =TopicForm(instance=topic)
        else:
            form =TopicForm(request.FILES,instance=topic,data=request.POST)    
            if form.is_valid():
                form.save()
                return redirect('study_log_app:topic',topic_id=topic.id)    

        context={'topic':topic, 'form':form}
        return render(request,'study_log_app/edit_topic.html',context)
                

@login_required
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm() 
    else:
        form =EntryForm(request.POST,request.FILES)  
        if form.is_valid():
            new_entry =  form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('study_log_app:topic',topic_id = topic.id)
    context = {'topic':topic,'form':form}  
    return render(request,'study_log_app/new_entry.html',context) 


@login_required
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic =entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form =EntryForm(instance=entry)
    else:
        form =EntryForm(request.FILES,instance=entry,data=request.POST)    
        if form.is_valid():
            form.save()
            return redirect('study_log_app:topic',topic_id = topic.id)    

    context={'entry':entry,'topic':topic, 'form':form}
    return render(request,'study_log_app/edit_entry.html',context)

# def delete_topic(request):

       





