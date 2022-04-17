from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

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
    return render(request,'profile.html')



#Use this for sending messages after POST

# message.debug
# message.info
# message.success
# message.warning
# message.error

