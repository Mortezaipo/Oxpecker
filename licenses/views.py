from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import Http404
from models import License
from forms import LicenseForm



def index(request):
    data = {'licenses': License.objects.all()}
    return render(request, 'licenses/index.html', data)


def new(request):
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'New license has been added successfully.')
            return redirect(reverse('licenses_index'))
    else:
        form = LicenseForm()
    data = {'form': form}
    return render(request, 'licenses/new.html', data)


def destroy(request, lid):
    data = {}
    try:
        license = License.objects.get(id=lid)
    except License.DoesNotExist:
        raise Http404('License Not Found!')
    if request.method == 'POST':
        try:
            row = License.objects.get(id=lid)
            row.delete()
            messages.add_message(request, messages.SUCCESS, '%s license has been removed.' % license.name)
        except License.DoesNotExist:
            messages.add_message(request, messages.ERROR, '%s license not found.' % license.name)
        return redirect(reverse('licenses_index'))
    data.update({'license': license})
    return render(request, 'licenses/destroy.html', data)


def edit(request, lid):
    data = {}
    try:
        license = License.objects.get(id=lid)
    except License.DoesNotExist:
        raise Http404('License Not Found!')
    if request.method == 'POST':
        form = LicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '%s license has been updated successfully.' % license.name)
            return redirect(reverse('licenses_index'))
    else:
        form = LicenseForm(instance=license)
        
    data.update({'license':license})
    data.update({'form': form})
    return render(request, 'licenses/edit.html', data)
