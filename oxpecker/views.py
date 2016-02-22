from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from users.forms import RegisterForm
from django.contrib import messages


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