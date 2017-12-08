from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^feedback/',views.feedback,name='feedback'),
    url(r'^guestbook/create/', views.create, name='create'),
    url(r'^guestbook/save/', views.save, name='save'),
]
