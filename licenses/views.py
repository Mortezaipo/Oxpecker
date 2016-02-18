from django.shortcuts import render
from models import License
from forms import LicenseForm


def index(request):
    data = {'licenses': License.objects.all()}
    return render(request, 'licenses/index.html', data)
