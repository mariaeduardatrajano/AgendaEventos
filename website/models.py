from django.db import models

class Evento(models.Model):
  nome = models.CharField(max_length=255)
  descricao = models.TextField()
  data_hora = models.DateTimeField()
  organizadores = models.ManyToManyField('Organizador')
  participantes = models.ManyToManyField('Participante')
  local = models.OneToOneField('Local', on_delete=models.CASCADE)

class Organizador(models.Model):
  nome = models.CharField(max_length=255)
  idade = models.IntegerField()

class Participante(models.Model):
  nome = models.CharField(max_length=255)
  idade = models.IntegerField()

class Local(models.Model):
  nome = models.CharField(max_length=255)
  endereco = models.CharField(max_length=255)
  capacidade = models.IntegerField()