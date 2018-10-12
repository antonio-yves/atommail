from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as atommail

app_name = 'atommail'

urlpatterns = [
	path('', atommail.Home.as_view(), name='home'),
	path('new/message', atommail.NewMessage.as_view(), name='new-message'),
	path('profile/<pk>', atommail.Profile.as_view(), name='profile'),
	path('profile/<pk>/view', atommail.ViewProfile.as_view(), name='view-profile'),
	path('add/friend/<pk>', atommail.AddFriend.as_view(), name='add-friend'),
	path('message/<pk>/read', atommail.ReadMessage.as_view(), name='read-message'),
	path('messages/sent', atommail.SentMessage.as_view(), name='sent'),
]