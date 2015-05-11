from django.conf.urls import url, patterns
from django.views.generic import TemplateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gatofan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Users URLS
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
)
