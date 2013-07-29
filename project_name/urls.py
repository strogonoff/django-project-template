from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from . import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(), name='home'),
    #url(r'^news/', include('{{ project_name }}.news.urls')),

    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
