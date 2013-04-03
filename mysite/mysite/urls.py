from django.conf.urls import patterns, include, url
from mysite.view import current_datetime
from mysite.view import home
from mysite.view import login
from mysite.view import login_to_home
from mysite.view import logout
from mysite.view import publish
from books.views import search

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^time$',current_datetime),
    (r'^home$',home),
    (r'^search$',search),
	(r'^login$',login),
	(r'^login_to_home$',login_to_home),
	(r'^logout$',logout),
	(r'^$',home),
	(r'^publish$',publish),
)
