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
from games import views as game_views
from companies import views as company_views
from oxpecker import views as oxpecker_views
from django.contrib.auth.views import login, logout_then_login
from django.conf.urls.static import static #FIXME: just for development
from django.conf import settings #FIXME: just for development

urlpatterns = [
    # Home
    url(r'^$', oxpecker_views.index, name="home"),
    
    #Authentication
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^register/$', oxpecker_views.register, name="register"),
    url(r'^profile/$', oxpecker_views.profile, name="profile"),
    
    # License
    url(r'^licenses/$', license_views.index, name="licenses_index"),
    url(r'^licenses/new$', license_views.new, name="licenses_new"),
    url(r'^licenses/(?P<lid>\d+)/destroy$', license_views.destroy, name="licenses_destroy"),
    url(r'^licenses/(?P<lid>\d+)/edit$', license_views.edit, name="licenses_edit"),
    url(r'^licenses/(?P<lid>\d+)/$', license_views.printing, name="licenses_print"),
    
    # Game
    url(r'^games/$', game_views.index, name="games_index"),
    url(r'^games/new$', game_views.new, name="games_new"),
    url(r'^games/versions/(?P<gid>\d+)/$', game_views.version, name="games_versions_index"),
    url(r'^games/versions/(?P<gid>\d+)/new$', game_views.new_version, name="games_versions_new"),
    
    
    # Company
    url(r'^companies/$', company_views.index, name="companies_index"),
    url(r'^companies/(?P<cid>\w+)/$', company_views.info, name="companies_info"),
    url(r'^companies/new$', company_views.new, name="companies_new"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #FIXME: just for development
