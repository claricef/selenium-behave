from behave import given, when, then
# features/steps/login_valido_step.py

@when('ele preenche seu usuário "{usuario}" e a senha incorreta "{senha}"')
def step_preencher_campos_login(context, usuario, senha):
    context.pageLogin.preencher_login_usuario_cadastrado(usuario, senha)

@then('ele deve ser visualizar uma mensagem de usuário ou senha inválidos')
def step_verificar_login_invalido(context):
    context.pageLogin.buscar_mensagem_login_invalido()
 