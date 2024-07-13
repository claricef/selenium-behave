from behave import given, when, then
from pages.inventario_item_page import InventarioItemPage
from pages.carrinho_page import CarrinhoPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

# features/steps/adicionar_item_carrinho_step.py

@when('acessar o carrinho')
def step_acessar_carrinho(context):
    pageInventarioItem = InventarioItemPage(context.browser)
    pageInventarioItem.acessar_carrinho()

@when('realizar o checkout fornecendo o "{nome}", "{sobrenome}" e "{cep}"')
def step_realizar_checkout(context, nome, sobrenome, cep):
    pageCarrinho = CarrinhoPage(context.browser)
    pageCarrinho.realizar_checkout()
    pageCheckout = CheckoutPage(context.browser)
    pageCheckout.preencher_checkout(nome,sobrenome,cep)
    pageCheckout.finalizar_checkout()

@when('finalizar a compra')
def step_finalizar_compra(context):
    pageCheckoutOverview = CheckoutOverviewPage(context.browser)
    pageCheckoutOverview.finalizar_compra()
    
@then('ele será redirecionado para a tela de checkout completo')
def step_verificar_pagina_checkout_completo(context):
    pageCheckoutComplete = CheckoutCompletePage(context.browser)
    pageCheckoutComplete.buscar_mensagem_checkout_complete()