from django.contrib import admin
from olha_boca.pessoas.models import Pessoa

# Register your models here.

class PessoasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'infracoes_a_pagar', 'total_infracoes', 'valor_a_pagar')

    @admin.display(empty_value='???')
    def total_infracoes(self, obj):
        return obj.infracoes.count()

    @admin.display(empty_value='???')
    def infracoes_a_pagar(self, obj):
        return obj.infracoes.filter(paga=False).count()

    @admin.display(empty_value='???')
    def valor_a_pagar(self, obj):
        total = 0
        infracoes_a_pagar = obj.infracoes.filter(paga=False).all()
        for inf in infracoes_a_pagar:
            total += (inf.tipo.vibs * inf.tipo.multiplicador_vibs)
        return f'R$ {total:.2f}'

admin.site.register(Pessoa, PessoasAdmin)