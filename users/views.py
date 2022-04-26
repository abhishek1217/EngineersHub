from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from QES.models import Questions,Answers
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm


def register(request): #For registering as a new user
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()        
    
    return render(request,'signup.html',{'form': form})

@login_required
def profile(request): #Update Profile
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'You Profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'profile.html', context)

def logout_view(request): #Logout
    Questions.objects.all().update(downvoted='False')
    Answers.objects.all().update(downvoted='False')
    userid = request.user.id
    rep = 0
    for quest in Questions.objects.all():
        if quest.author_id == userid:
            rep += quest.totalvotes
    for answer in Answers.objects.all():
        if answer.author_id == userid:
            rep += quest.totalvotes
    Profile.objects.filter(user_id=userid).update(reputation=rep)
    logout(request)
    return redirect('login')

