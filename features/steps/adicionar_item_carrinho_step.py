from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventorario_page import InventarioPage

@given('que o "{usuario}" logado com sua "{senha}" acesse a pagina de inventario')
def step_acessar_pagina_inventario(context, usuario, senha):
    pageLogin = LoginPage(context.browser)
    pageLogin.acessar_pagina("/")
    context.pageLogin = pageLogin
    context.pageLogin.preencher_login_usuario_cadastrado(usuario, senha)
    context.pageLogin.acessar_sistema()

@when('ele clicar para adicionar o produto ao carrinho')
def step_adicionar_item_carrinho(context):
    pageInventario = InventarioPage(context.browser)
    pageInventario.adicionar_item_carrinho()

@then('ele deve ver o icone indicando presença de produto no carinho')
def step_verificar_icone_item_adicionar(context):
    pageInventario = InventarioPage(context.browser)
    pageInventario.buscar_icone_item_adicionado() 