# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from palpite.models import PalpiteDoParticipante

class Rodada(models.Model):
	descricao = models.CharField(max_length=100)
	participantes = models.ManyToManyField(User, related_name="rodada_participantes")

	def __unicode__(self):
		return self.descricao

class Concurso(models.Model):
	numero = models.IntegerField()
	premio_estimativa = models.IntegerField()
	rodada = models.ForeignKey(Rodada)

	def __unicode__(self):
		return str(self.numero)


class Jogo(models.Model):
	numero = models.IntegerField()
	coluna1 = models.CharField(max_length=100)
	coluna2 = models.CharField(max_length=100)
	concurso = models.ForeignKey(Concurso)
	palpitedoparticipante = models.ForeignKey(PalpiteDoParticipante)
	palpite = models.IntegerField()


	def __unicode__(self):
		return str(self.numero)

