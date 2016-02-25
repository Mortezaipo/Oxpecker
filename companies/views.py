from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from forms import CompanyForm, DeveloperForm
from models import Company, Developer
from django.forms import formset_factory


def index(request):
    companies = Company.objects.filter(user=request.user)
    data = {'companies': companies}
    return render(request, 'companies/index.html', data)


def new(request):
    company_form = CompanyForm()
    developer_form = formset_factory(DeveloperForm, min_num=1)
    
    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES)
        developer_form = developer_form(request.POST, request.FILES)
        
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.user = request.user
            company.save()
            
            if developer_form.is_valid():
                for dev in developer_form:
                    action = dev.save(commit=False)
                    action.company = company
                    action.save()
                messages.add_message(request, messages.SUCCESS, "New company with its team memebers have been saved successfully.")
                return redirect(reverse('companies_index'))
            else:
                company.delete()
                messages.add_message(request, messages.ERROR, "Team memebers saving failed. Check yout data.")
        else:
            messages.add_message(request, messages.ERROR, "Add new company failed. Check yout data.")
    data = {'company_form': company_form, 'developer_form': developer_form}
    return render(request, 'companies/new.html', data)