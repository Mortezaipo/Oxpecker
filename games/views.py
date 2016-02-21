from django.shortcuts import render
from forms import GameForm
from django.contrib import messages


def index(request):
    pass


def new(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "New game has been added successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Add new game failed. Check yout data.")            
    else:
        form = GameForm()
    
    data = {'form': form}
    return render(request, 'games/new.html', data)