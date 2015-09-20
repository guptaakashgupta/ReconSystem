from django.conf.urls import patterns, include, url
from django.contrib import admin
from recon import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ReconSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',views.index_view),
    url(r'',views.home_view)

)
