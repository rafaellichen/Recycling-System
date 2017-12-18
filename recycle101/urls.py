from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recycle101', views.index, name='index'),
    url(r'^search/', views.searchHowTo, name='searchHowTo')    
]
