"""oxpecker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from licenses import views as license_views

urlpatterns = [
    url(r'^licenses/$', license_views.index, name="licenses_index"),
    url(r'^licenses/new$', license_views.new, name="licenses_new"),
    url(r'^licenses/(?P<lid>\d+)/destroy$', license_views.destroy, name="licenses_destroy"),
    url(r'^licenses/(?P<lid>\d+)/edit$', license_views.edit, name="licenses_edit"),
]
