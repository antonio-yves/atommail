# AtomMail

O AtomMail é um projeto dos alunos Antonio Yves, Ítalo André, Maria Francisca e Rafael Almeida do 4º INTIN 2018 do IFPB - Campus Cajazeiras. Que buscaram desenvolver um sistema de mensagens usando o Framework Django com criptografia de Chave Pública e Privada.

## Sobre o Desenvolvimento
> Projeto desenvolvido em Django e utiliza banco de dados PostgreSQL para armazenar as chaves privadas.

## models.py
O sistema possui três classes responsáveis pela criação do banco de dados, uma é responsável pelo salvamento das mensagens criptografadas (Models Message), outra para salvar os contatos de cada usuário (Models Contact) e por último uma que armazena as chaves públicas dos usuários.

```python
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
```

```python
class Contact(CreateUpdateModel):
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'users', verbose_name = 'usuário')
	contact = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'contacts', verbose_name = 'contato')

	def __str__(self):
		return 'Contato do usuário: %s' % self.user.username

	class Meta:
		verbose_name = 'contato'
		verbose_name_plural = 'contatos'
```

```python
class PublicKey(CreateUpdateModel):
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'user', verbose_name = 'dono da chave')
	key = models.BinaryField(max_length = None, verbose_name = 'chave pública')

	def __str__(self):
		return 'Chave Pública do Usuário: ' + self.user.username

	class Meta:
		verbose_name = 'chave pública'
		verbose_name_plural = 'chaves públicas'
```

## Banco de Dados PostgreSQL
> O arquivo para a geração do banco de dados do PostgreSQL, encontra-se na pasta 'bd'.

## Testando
Para testar e conhecer o projeto, você deve realizar o seguinte passo a passo:
1. Clone o projeto para o seu computador:
> git clone https://github.com/antonio-yves/atommail.git
2. Instale as dependências do projeto:
> pip install -r requeriments.txt
3. Realize a criação do banco de dados, caso você tenha excluído o arquivo "db.sqlite3". Execute os comandos nessa ordem:
> python manage.py migrate
4. Instale o PostgreSQL e crie o banco de dados com o arquivo 'bd.sql' que está na pasta 'bd'.
5. Altere o usuário e a senha de conexo do banco externo nas View:
> app/atommail/views.py | class ReadMessage() - linha 60;
>
>app/core/views.py | class UserCreateView() - linha 26;
6. Crie um super usuário (Administrador):
> python manage.py createsuperuser
7. Execute o projeto:
> python manage.py runserver
8. Aproveite!


