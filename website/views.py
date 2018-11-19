from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from empresa_xyz.models import Empresa, Servico, Vendedor, Venda
from website.forms import InsereEmpresaForm, InsereServicoForm, InsereVendedorForm, InsereVendaForm
from django.shortcuts import render


# PÁGINA PRINCIPAL
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE EMPRESAS
class EmpresaListView(ListView):
    template_name = "website/lista.html"
    model = Empresa
    context_object_name = "empresas"


# CADASTRAMENTO DE EMPRESAS
class EmpresaCreateView(CreateView):
    template_name = "website/cria.html"
    model = Empresa
    form_class = InsereEmpresaForm
    success_url = reverse_lazy("website:lista_empresas")


# ATUALIZAÇÃO DE EMPRESAS
class EmpresaUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Empresa
    fields = '__all__'
    context_object_name = 'empresa'
    success_url = reverse_lazy("website:lista_empresas")


# EXCLUSÃO DE EMPRESAS
class EmpresaDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Empresa
    context_object_name = 'empresa'
    success_url = reverse_lazy("website:lista_empresas")

########################################################

# LISTA DE SERVICOS
class ServicoListView(ListView):
    template_name = "website/lista_servico.html"
    model = Servico
    context_object_name = "servicos"


# CADASTRAMENTO DE SERVICOS
class ServicoCreateView(CreateView):
    template_name = "website/cria_servico.html"
    model = Servico
    form_class = InsereServicoForm
    success_url = reverse_lazy("website:lista_servicos")


# ATUALIZAÇÃO DE SERVICOS
class ServicoUpdateView(UpdateView):
    template_name = "website/atualiza_servico.html"
    model = Servico
    fields = '__all__'
    context_object_name = 'servico'
    success_url = reverse_lazy("website:lista_servicos")


# EXCLUSÃO DE SERVICOS
class ServicoDeleteView(DeleteView):
    template_name = "website/exclui_servico.html"
    model = Servico
    context_object_name = 'servico'
    success_url = reverse_lazy("website:lista_servicos")

###########################################################

# LISTA DE VENDEDORES
class VendedorListView(ListView):
    template_name = "website/lista_vendedor.html"
    model = Vendedor
    context_object_name = "vendedores"


# CADASTRAMENTO DE VENDEDORES
class VendedorCreateView(CreateView):
    template_name = "website/cria_vendedor.html"
    model = Vendedor
    form_class = InsereVendedorForm
    success_url = reverse_lazy("website:lista_vendedores")


# ATUALIZAÇÃO DE VENDEDORES
class VendedorUpdateView(UpdateView):
    template_name = "website/atualiza_vendedor.html"
    model = Vendedor
    fields = '__all__'
    context_object_name = 'vendedor'
    success_url = reverse_lazy("website:lista_vendedores")


# EXCLUSÃO DE VENDEDORES
class VendedorDeleteView(DeleteView):
    template_name = "website/exclui_vendedor.html"
    model = Vendedor
    context_object_name = 'vendedor'
    success_url = reverse_lazy("website:lista_vendedores")


###########################################################

# VENDAS REALIZADAS
class VendaListView(ListView):
    template_name = "website/lista_venda.html"
    model = Venda
    context_object_name = "vendas"

# CADASTRAMENTO DE VENDAS
class VendaCreateView(CreateView):
    template_name = "website/cria_venda.html"
    model = Venda
    form_class = InsereVendaForm
    success_url = reverse_lazy("website:lista_vendas")

# ATUALIZAÇÃO DE VENDAS
class VendaUpdateView(UpdateView):
    template_name = "website/atualiza_venda.html"
    model = Venda
    fields = '__all__'
    context_object_name = 'venda'
    success_url = reverse_lazy("website:lista_vendas")

# EXCLUSÃO DE VENDAS
class VendaDeleteView(DeleteView):
    template_name = "website/exclui_venda.html"
    model = Venda
    context_object_name = 'venda'
    success_url = reverse_lazy("website:lista_vendas")

###########################################################

'''def VendedorEmpresa(request):
    vendedores = Vendedor.objetos.all()

    contexto = {
        'vendedores': vendedores
    }

    return render(
        request,
        "templates/vendedor_empresa.html",
        contexto
    )'''

'''class VendedorEmpresa(UpdateView):
    template_name = "website/vendedor_empresa.html"
    model = Vendedor
    fields = '__all__'
    context_object_name = "vendedores"

    def get_object(self, queryset=None, nome_empresa):
        vendedor = None
        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            vendedor = Vendedor.objetos.filter(id=id).filter(empresa_vendedor=nome_empresa).all()

        return vendedor'''