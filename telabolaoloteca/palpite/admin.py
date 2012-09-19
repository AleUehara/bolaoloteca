from django.contrib import admin
from django import forms
from palpite.models import PalpiteDoParticipante
from cadastro.models import JogoDoParticipante

class JogoDoParticipanteInline(admin.TabularInline):
    model = JogoDoParticipante
    readonly_fields = ('numero', 'coluna1', 'coluna2', 'concurso')


class PalpiteDoParticipanteAdmin(admin.ModelAdmin):
    inlines = [
        JogoDoParticipanteInline,
    ]


admin.site.register(PalpiteDoParticipante, PalpiteDoParticipanteAdmin)

