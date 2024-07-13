from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventario_page import InventarioPage
from pages.inventario_item_page import InventarioItemPage

@given('que o "{usuario}" logado com sua "{senha}" acesse a pagina de inventario')
def step_acessar_pagina_inventario(context, usuario, senha):
    pageLogin = LoginPage(context.browser)
    pageLogin.acessar_pagina("/")
    context.pageLogin = pageLogin
    context.pageLogin.preencher_login_usuario_cadastrado(usuario, senha)
    context.pageLogin.acessar_sistema()

@when('ele acessar o produto')
def step_acessar_item(context):
    pageInventario = InventarioPage(context.browser)
    pageInventario.acessar_item()

@when('clicar para adicionar o produto ao carrinho')
def step_adicionar_item_carrinho(context):
    pageInventarioItem = InventarioItemPage(context.browser)
    pageInventarioItem.adicionar_item_carrinho()

@then('ele deve ver o icone indicando presença de produto no carinho')
def step_verificar_icone_item_adicionar(context):
    pageInventarioItem = InventarioItemPage(context.browser)
    pageInventarioItem.buscar_icone_item_adicionado() 