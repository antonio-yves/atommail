from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models

class Home(TemplateView):
    template_name = 'atommail/email.html'
    