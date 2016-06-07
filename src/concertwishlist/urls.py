from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'concertwishlist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'wishlist.views.home', name='home'),
    url(r'^event/(?P<eventId>(\d+))/$', 'wishlist.views.event', name='event'),

    url(r'^admin/', include(admin.site.urls)),
]
