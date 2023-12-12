from django.shortcuts import render , redirect
from accounts.forms import EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from django.views.generic import TemplateView 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def home(request):
    return render(request, 'accounts/home.html' )

@login_required
def view_profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html',args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form=EditProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('view_profile')
        else:
            pass
    else:
        form=EditProfileForm(instance=request.user.userprofile)
        args={'form':form}
        return render(request, 'accounts/edit_profile.html',args)
    

@login_required
def view_people(request):
    profile_list = UserProfile.objects.all()
    return render(request,'accounts/people.html',{'profile_list':profile_list})
