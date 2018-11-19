from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    objetos = models.Manager()


class Servico(models.Model):
    nome_servico = models.CharField(max_length=100, null=False, blank=False)
    empresa_prestadora = models.CharField(max_length=100, null=False, blank=False)
    comissao_servico = models.IntegerField(default=0, null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    objetos = models.Manager()

    #def __init__(self):
     #   self.calculo_comissao = self.preco*self.comissao_servico/100


class Vendedor(models.Model):
    nome_vendedor = models.CharField(max_length=100, null=False, blank=False)
    comissao_vendedor = models.DecimalField(max_digits=10, default=0.0, decimal_places=2, null=False, blank=False)
    empresa_vendedor = models.CharField(max_length=100, null=False, blank=False)
    objetos = models.Manager()


class Venda(models.Model):
    id_vendedor = models.CharField(default="nenhum", max_length=100, null=False)
    id_servico = models.CharField(max_length=100, null=False, blank=False)
    id_empresa = models.CharField(max_length=100, null=False, blank=False)