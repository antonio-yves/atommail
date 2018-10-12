from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
import psycopg2
import psycopg2.extras
from .models import *
from .cripto import *
from Crypto.PublicKey import RSA

class Home(LoginRequiredMixin, View):
	def get(self, request):
		mensagens = Message.objects.filter(recipient = self.request.user, status = 0)
		return render(request, 'email/index.html', {'mensagens': mensagens})

class NewMessage(LoginRequiredMixin, View):
	def get(self, request):
		contatos = Contact.objects.filter(user = self.request.user)
		return render(request, 'email/compose.html', {'contatos': contatos})

	def post(self, request):
		print(type(request.POST.get('contato')))
		destinatario = UUIDUser.objects.filter(id = request.POST.get('contato')).first()
		chave_publica = PublicKey.objects.filter(user = destinatario).first()
		publick_key = RSA.importKey(chave_publica.key)
		mensagem = Message(sender = self.request.user, recipient = destinatario, subject = request.POST.get('assunto'), message = encrypt(str.encode(request.POST.get('mensagem')), publick_key))
		mensagem.save()
		return redirect('atommail:home')

class Profile(LoginRequiredMixin, View):
	def get(self, request, pk):
		contatos = Contact.objects.filter(user = self.request.user)
		users = UUIDUser.objects.all().exclude(username = self.request.user.username)
		return render(request, 'email/profile.html', {'contatos': contatos, 'usuarios': users})
	
	def post(self, request):
		return render(request, 'email/profile.html')

class ViewProfile(LoginRequiredMixin, View):
	def get(self, request, pk):
		user = UUIDUser.objects.filter(id = pk).first()
		contatos = Contact.objects.filter(user = user)
		friend = Contact.objects.filter(user = user, contact = self.request.user)
		if len(friend) != 0:
			return render(request, 'email/profile.html', {'contatos': contatos, 'pessoa': user, 'friend': friend})
		return render(request, 'email/profile.html', {'contatos': contatos, 'pessoa': user})

class AddFriend(LoginRequiredMixin, View):
	def get(self, request, pk):
		pessoa = UUIDUser.objects.filter(id = pk).first()
		contato = Contact(user = self.request.user, contact = pessoa)
		contato.save()
		return redirect('atommail:profile', pk = self.request.user.pk)

class ReadMessage(LoginRequiredMixin, View):
	def get(self, request, pk):
		mensagem_criptografada = Message.objects.filter(id = pk).first()
		db = psycopg2.connect("dbname=chaves_privadas user=postgres password=sousa123 host=127.0.0.1")
		db.autocommit = True
		cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cur.execute("SELECT * from keys WHERE usuario = '{}'".format(str(self.request.user.pk)))
		chave = cur.fetchone()
		cur.close()
		db.close()
		chave_privada = RSA.importKey(str.encode(chave['chave']))
		mensagem_descriptografada = decrypt(mensagem_criptografada.message, chave_privada)
		print(mensagem_descriptografada.decode())
		return render(request, 'email/read-mail.html', {'mensagem_criptografada': mensagem_criptografada, 'mensagem_descriptografada': mensagem_descriptografada.decode()})

class SentMessage(LoginRequiredMixin, View):
	def get(self, request):
		mensagens = Message.objects.filter(sender = self.request.user, status = 0)
		return render(request, 'email/sent.html', {'mensagens': mensagens})
