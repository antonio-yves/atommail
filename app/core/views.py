from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
from .forms import RegistrationUserForm
from app.atommail.cripto import *
from app.atommail.models import PublicKey
import psycopg2
import psycopg2.extras

class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')
    form_class = RegistrationUserForm

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.set_password(obj.password)
    	obj.save()
    	chave_publica, chave_privada = geradorChaves(2048)
    	public_key = PublicKey(user = obj, key = chave_publica.exportKey())
    	public_key.save()
    	db = psycopg2.connect("dbname=chaves_privadas user=postgres password=sousa123 host=127.0.0.1")
    	db.autocommit = True
    	cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    	cur.execute("INSERT INTO keys (usuario, chave) VALUES ('{}', '{}')".format(str(obj.pk), chave_privada.exportKey().decode()))
    	cur.close()
    	db.close()
    	return super(UserCreateView, self).form_valid(form)

