CREATE DATABASE CHAVES_PRIVADAS;

CREATE TABLE KEYS(
	id_chave serial,
	usuario varchar(255),
	chave text,
	primary key (id_chave)
);