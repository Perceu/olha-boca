from django.contrib import admin
from olha_boca.infracoes.models import Infracoes, InfracoesTipos


@admin.action(description='Marcar como paga')
def pagar(modeladmin, request, queryset):
    queryset.update(paga=True)

class InfracoesAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'tipo', 'paga', 'valor')
    list_filter = ('pessoa',)
    actions = [pagar]

    @admin.display(empty_value='???')
    def valor(self, obj):
        total = obj.tipo.vibs * obj.tipo.multiplicador_vibs
        return f'R$ {total:.2f}'

admin.site.register(Infracoes, InfracoesAdmin)

class InfracoesTiposAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'vibs', 'multiplicador_vibs', 'valor')
    search_fields = ('tipo',)

    @admin.display(empty_value='???')
    def valor(self, obj):
        total = obj.vibs * obj.multiplicador_vibs
        return f'R$ {total:.2f}'

admin.site.register(InfracoesTipos, InfracoesTiposAdmin)