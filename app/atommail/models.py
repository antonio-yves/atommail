from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Message(CreateUpdateModel):
	STATUS = (
	(0, 'Caixa Principal/Enviada'),
	(1, 'Lixeira')
	)
	sender = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'senders', verbose_name = 'remetente')
	recipient = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'recipients', verbose_name = 'destinatário')
	subject = models.CharField(max_length = 255, verbose_name = 'assunto', blank = True, null = True)
	message = models.BinaryField(max_length = None, verbose_name = 'mensagem', blank = True, null = True)
	sent = models.DateTimeField(auto_now_add = True, verbose_name = 'Enviado em')
	status = models.IntegerField(choices = STATUS, verbose_name = 'Status', default = 0)

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

class PublicKey(CreateUpdateModel):
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'user', verbose_name = 'dono da chave')
	key = models.BinaryField(max_length = None, verbose_name = 'chave pública')

	def __str__(self):
		return 'Chave Pública do Usuário: ' + self.user.username

	class Meta:
		verbose_name = 'chave pública'
		verbose_name_plural = 'chaves públicas'