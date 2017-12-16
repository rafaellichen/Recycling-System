'''URLS for mainRecycleApp'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^search/', views.search_withQuery, name='search_withQuery'),
    url(r'^donation/(?P<id>\d+)/$', views.donationSiteDetails, name='donationSiteDetails')    
]
