from django.contrib import admin
from palpite.models import PalpiteDoParticipante
from cadastro.admin import JogoInline


class PalpiteDoParticipanteAdmin(admin.ModelAdmin):
    inlines = [
        JogoInline,
    ]

admin.site.register(PalpiteDoParticipante, PalpiteDoParticipanteAdmin)

