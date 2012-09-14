from django.contrib import admin
from cadastro.models import Rodada, Concurso, Jogo

class JogoInline(admin.TabularInline):
    model = Jogo

class ConcursoAdmin(admin.ModelAdmin):
    inlines = [
        JogoInline,
    ]

#admin.site.unregister(Rodada)
admin.site.register(Rodada)
admin.site.register(Concurso, ConcursoAdmin)


