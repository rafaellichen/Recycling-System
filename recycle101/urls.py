from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^recycle101$', views.index, name='index'),
    url(r'^recycle101/search/', views.searchHowTo, name='searchHowTo')    
]
