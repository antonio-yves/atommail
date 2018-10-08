from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Message(CreateUpdateModel):
	sender = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'senders', verbose_name = 'remetente')
	recipient = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'recipients', verbose_name = 'destinatário')
	subject = models.CharField(max_length = 255, verbose_name = 'assunto')
	message = models.TextField(verbose_name = 'mensagem', blank = True, null = True)
	media = models.FileField(upload_to = 'medias/', blank = True, null = True)

	def __str__(self):
		return 'Mensagem do Usuário: %s Para %s' % (self.sender.username, self.recipient.username)

	class Meta:
		verbose_name = 'mensagem'
		verbose_name_plural = 'mensagens'

class Contact(CreateUpdateModel):
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'users', verbose_name = 'usuário')
	contact = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'contacts', verbose_name = 'contato')

	def __str__(self):
		return 'Contato do usuário: %s' % self.user.username

	class Meta:
		verbose_name = 'contato'
		verbose_name_plural = 'contatos'
