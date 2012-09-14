from django.db import models
from django.contrib.auth.models import User

class PalpiteDoParticipante(models.Model):
	participante = models.ForeignKey(User)

