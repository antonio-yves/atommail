from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as atommail

app_name = 'atommail'

urlpatterns = [
	path('', atommail.Home.as_view(), name='home'),
]