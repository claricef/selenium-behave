from behave import given, when, then
from pages.login_page import LoginPage

@given('que o usuario acessa a pagina de login')
def step_acessar_pagina_login(context):
    pageLogin = LoginPage(context.browser)
    pageLogin.acessar_pagina("/")
    context.pageLogin = pageLogin

@when('ele preenche seu usuário "{usuario}" e sua senha "{senha}"')
def step_preencher_campos_login(context, usuario, senha):
    context.pageLogin.preencher_login_usuario_cadastrado(usuario, senha)

@when('ele aciona a opção para logar')
def step_clicar_realizar_login(context):
    context.pageLogin.acessar_sistema()

@then('ele deve ser redirecionado para a página inicial de usuário logado')
def step_verificar_login_sucesso(context):
    pass