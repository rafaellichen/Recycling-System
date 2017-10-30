from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^/about/$', views.about, name='about'),
=======
>>>>>>> 5864c299cd6050e292038c3ece7ca99e0b0fae77
]
