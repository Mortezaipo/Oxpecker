from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import Game, Version
from forms import GameForm, ScreenshotForm, VersionForm
from django.contrib import messages
from django.forms import formset_factory
from django.http import Http404


def index(request):
    games = Game.objects.order_by('-created_datetime')
    data = {'games': games}
    return render(request, 'games/index.html', data)


def new(request):
    game_form = GameForm(request.user)
    screenshot_form = formset_factory(ScreenshotForm, extra=4, min_num=4, max_num=8)
    
    if request.method == "POST":
        game_form = GameForm(request.user, request.POST, request.FILES)
        screenshot_form = screenshot_form(request.POST, request.FILES)
        
        if game_form.is_valid():
            game = game_form.save()
            
            if screenshot_form.is_valid():
                for scf in screenshot_form:
                    action = scf.save(commit=False)
                    if not action.image:
                        continue
                    action.game = game
                    action.save()
                messages.add_message(request, messages.SUCCESS, "New game has been added successfully.")
                return redirect(reverse('games_index'))
            else:
                game.delete()
                messages.add_message(request, messages.ERROR, "Add new game failed. Check your screenshots.")
        else:
            messages.add_message(request, messages.ERROR, "Add new game failed. Check your game data.")
            
    data = {'game_form': game_form, 'screenshot_form': screenshot_form}
    return render(request, 'games/new.html', data)


def version(request, gid):
    try:
        game = Game.objects.get(id=gid)
    except Game.DoesNotExists:
        raise Http404('Game not found!')

    data = {'versions': game.version_set.all()}
    return render(request, 'games/versions/index.html', data)

def new_version(request, gid):
    try:
        game = Game.objects.get(id=gid)
    except Game.DoesNotExists:
        raise Http404('Game not found!')
    
    form = VersionForm()
    if request.method == "POST":
        form = VersionForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.save(commit=False)
            action.game = game
            action.save()
            messages.add_message(request, messages.SUCCESS, "New version has been added successfully.")
            return redirect(reverse('versions_index', kwargs={'gid': gid}))
        else:
            messages.add_message(request, messages.ERROR, "Add new version failed. Check your data.")
    
    data = {'form': form, 'gid': gid}
    return render(request, 'games/versions/new.html', data)