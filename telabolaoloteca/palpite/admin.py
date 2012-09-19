from django.contrib import admin
from django import forms
from palpite.models import PalpiteDoParticipante
from cadastro.models import JogoDoParticipante, Concurso

class JogoDoParticipanteForm(forms.ModelForm):
    def __init__(self, logged_in_user, *args, **kwargs):
      super(self.__class__, self).__init__(*args, **kwargs)
      #self.fields['numero'].initial = logged_in_user
#	numero = forms.CharField(initial=Concurso.objects.all().order_by("-numero")[0] )
    #model = JogoDoParticipante
    #class Meta:
    #	model = JogoDoParticipante

class JogoDoParticipanteInline(admin.TabularInline):
    model = JogoDoParticipante
    readonly_fields = ('numero', 'coluna1', 'coluna2', 'concurso')
    max_num = 14
    extra = 14
    #form = JogoDoParticipanteForm(1)
    #form = JogoDoParticipanteForms
    #fields = ('numero', 'coluna1', 'coluna2', 'concurso')



class PalpiteDoParticipanteAdmin(admin.ModelAdmin):
    inlines = [
        JogoDoParticipanteInline,
    ]

    print inlines[0].model
    print len(inlines)
    #print self.form.declared_fields['numero'].initial


admin.site.register(PalpiteDoParticipante, PalpiteDoParticipanteAdmin)

