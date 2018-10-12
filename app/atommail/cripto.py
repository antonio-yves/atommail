from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from base64 import b64encode, b64decode

def geradorChaves(tamanho_chave):
	#2048
	random_generator = Random.new().read
	# criando as chaves. tamanho fixo.
	key = RSA.generate(tamanho_chave, random_generator)
	# chaves publica e privada
	private = key
	public = key.publickey()
	return public, private

def encrypt(mensagem, chave_publica):
	#RSA - implementação PKCS#1 OAEP
	cipher = PKCS1_OAEP.new(chave_publica)
	return cipher.encrypt(mensagem)

def decrypt(mensagem, chave_privada):
	#RSA - implementação PKCS#1 OAEP
	cipher = PKCS1_OAEP.new(chave_privada)
	return cipher.decrypt(mensagem)