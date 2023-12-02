from django.db import models

class Evento(models.Model):
  nome = models.CharField(max_length=255)
  descricao = models.TextField()
  data_hora = models.DateTimeField(verbose_name='Data e hora')
  organizadores = models.ManyToManyField('Organizador')
  participantes = models.ManyToManyField('Participante')
  local = models.OneToOneField('Local', on_delete=models.CASCADE)

  def __str__(self):
    return self.nome

class Organizador(models.Model):
  nome = models.CharField(max_length=255)
  idade = models.IntegerField()

  def __str__(self):
    return self.nome

class Participante(models.Model):
  nome = models.CharField(max_length=255)
  idade = models.IntegerField()

  def __str__(self):
    return self.nome

class Local(models.Model):
  nome = models.CharField(max_length=255)
  endereco = models.CharField(max_length=255, verbose_name='Endereço')
  capacidade = models.IntegerField()

  def __str__(self):
    return self.nome