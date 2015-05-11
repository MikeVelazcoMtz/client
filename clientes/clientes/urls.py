from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clientes.views.home', name='home'),
    # url(r'^$', 'apps.views', name='home'),
    url(r'^', include('apps.clientes.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
