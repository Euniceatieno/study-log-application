from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def register(request):
    if request.method!='POST': 
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid:
            new_user=form.save()
            login(request,new_user)
            return redirect('study_log_app:index')    


    context={'form': form}
    return render(request,'registration/register.html',context)


