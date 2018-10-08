from django.db import models

class PublicKey(models.Model):
	key = models.CharField(max_length = 255)

	def __str__(self):
		return 'Chave Pública'
