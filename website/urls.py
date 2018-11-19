from website.views import IndexTemplateView, EmpresaListView, EmpresaUpdateView, EmpresaCreateView, \
    EmpresaDeleteView, ServicoListView, ServicoUpdateView, ServicoCreateView, ServicoDeleteView, \
    VendedorListView, VendedorUpdateView, VendedorCreateView, VendedorDeleteView, VendaListView, \
    VendaUpdateView, VendaCreateView, VendaDeleteView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /empresa/cadastrar
    path('empresa/cadastrar', EmpresaCreateView.as_view(), name="cadastra_empresa"),

    # GET /empresas
    path('empresas/', EmpresaListView.as_view(), name="lista_empresas"),

    # GET/POST /empresa/{pk}
    path('empresa/<pk>', EmpresaUpdateView.as_view(), name="atualiza_empresa"),

    # GET/POST /empresas/excluir/{pk}
    path('empresa/excluir/<pk>', EmpresaDeleteView.as_view(), name="deleta_empresa"),

    ##################################################################################

    # GET /servico/cadastrar
    path('servico/cadastrar', ServicoCreateView.as_view(), name="cadastra_servico"),

    # GET /servicos
    path('servicos/', ServicoListView.as_view(), name="lista_servicos"),

    # GET/POST /servico/{pk}
    path('servico/<pk>', ServicoUpdateView.as_view(), name="atualiza_servico"),

    # GET/POST /servicos/excluir/{pk}
    path('servico/excluir/<pk>', ServicoDeleteView.as_view(), name="deleta_servico"),

    ##################################################################################

    # GET /vendedor/cadastrar
    path('vendedor/cadastrar', VendedorCreateView.as_view(), name="cadastra_vendedor"),

    # GET /vendedores
    path('vendedores/', VendedorListView.as_view(), name="lista_vendedores"),

    # GET/POST /vendedor/{pk}
    path('vendedor/<pk>', VendedorUpdateView.as_view(), name="atualiza_vendedor"),

    # GET/POST /vendedores/excluir/{pk}
    path('vendedor/excluir/<pk>', VendedorDeleteView.as_view(), name="deleta_vendedor"),

    # Testando chamada de Vendedores por empresa
    #path('vendedores/', VendedorEmpresa.as_view(), name="vendedor_empresa")

    ##################################################################################

    # GET /venda/cadastrar
    path('venda/cadastrar', VendaCreateView.as_view(), name="cadastra_venda"),

    # GET /vendas
    path('vendas/', VendaListView.as_view(), name="lista_vendas"),

    # GET/POST /venda/{pk}
    path('venda/<pk>', VendaUpdateView.as_view(), name="atualiza_venda"),

    # GET/POST /vendas/excluir/{pk}
    path('venda/excluir/<pk>', VendaDeleteView.as_view(), name="deleta_venda"),

]
