from django.conf.urls import url, include
from . import views as userViews 

# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', userViews.index, name='index'),
    url(r'^login$', userViews.signin, name='login'),
    url(r'^logout$', userViews.signout, name='logout'),
    url(r'^signup$', userViews.signup, name='signup'),
    url(r'^profile$', userViews.profile, name='profile'),
    url(r'^profile/edit$', userViews.editProfile, name='editProfile'),
    url(r'^bookmarks$', userViews.bookmarkHandler, name='bookmarks'),
]
