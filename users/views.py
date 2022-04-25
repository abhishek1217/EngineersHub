from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from QES.models import Questions,Answers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

def register(request):
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
def profile(request):
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

def logout_view(request):
    logout(request)
    Questions.objects.all().update(downvoted='False')
    Answers.objects.all().update(downvoted='False')
    rep = Questions.totalvotes + Answers.totalvotes
    User.profile.reputation.update(reputation=rep)
    return redirect('home')


#Use this for sending messages after POST

# message.debug
# message.info
# message.success
# message.warning
# message.error

