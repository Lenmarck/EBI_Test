from empresa_xyz.models import Empresa, Servico, Vendedor, Venda
from django import forms


# FORMULÁRIO DE CADASTRO DE EMPRESAS

class InsereEmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa

        fields = [
            'nome',
            'cnpj',
        ]

# FORMULÁRIO DE CADASTRO DE EMPRESAS

class InsereServicoForm(forms.ModelForm):

    class Meta:
        model = Servico

        fields = [
            'nome_servico',
            'comissao_servico',
            'empresa_prestadora',
            'preco',
        ]

# FORMULÁRIO DE CADASTRO DE VENDEDORES

class InsereVendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor

        fields = [
            'nome_vendedor',
            'comissao_vendedor',
            'empresa_vendedor',
        ]

# FORMULÁRIO DE VENDAS

class InsereVendaForm(forms.ModelForm):

    class Meta:
        model = Venda

        fields = [
            'id_empresa',
            'id_vendedor',
            'id_servico',
        ]