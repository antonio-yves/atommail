from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
import psycopg2
import psycopg2.extras
from . import models

class Home(TemplateView):
    template_name = 'email/index.html'

class NewMessage(TemplateView):
	template_name = 'email/compose.html'

class Teste(View):
	def get(self, request):
		db = psycopg2.connect("dbname=teste user=postgres password=sousa123 host=127.0.0.1")
		cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cur.execute("INSERT INTO private_key (usuario, chave) VALUES (%s, %s)", (str(self.request.user.pk), 'okay'))
		cur.close()
		db.close()
		return redirect('atommail:home')
