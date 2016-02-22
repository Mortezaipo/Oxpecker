from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from users.forms import RegisterForm, ProfileForm
from django.contrib import messages


def index(request):
    return render(request, 'oxpecker/home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, "Your registration succed. We've sent a verification link to your email address.")
                return redirect(reverse('login'))
            except:
                pass
    else:
        form = RegisterForm()
        
    data = {'form': form}
    return render(request, 'registration/register.html', data)


def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, "Your profile has been updated successfully.")
                return redirect(reverse('profile'))
            except:
                pass
    else:
        form = ProfileForm(instance=request.user)
    
    data = {'form': form}
    return render(request, 'registration/profile.html', data)