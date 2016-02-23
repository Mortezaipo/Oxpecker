from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from forms import CompanyForm, DeveloperForm
from models import Company, Developer


def index(request):
    companies = Company.objects.filter(user=request.user)
    data = {'companies': companies}
    return render(request, 'companies/index.html', data)


def new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.save(commit=False)
            action.user = request.user
            action.save()
            messages.add_message(request, messages.SUCCESS, "New company has been added successfully.")
            return redirect(reverse('companies_index'))
        else:
            messages.add_message(request, messages.ERROR, "Add new company failed. Check yout data.")
    else:
        form = CompanyForm()
    data = {'form': form}
    return render(request, 'companies/new.html', data)