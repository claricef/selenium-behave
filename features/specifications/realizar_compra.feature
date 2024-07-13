@compra
Feature: Realizar compra 

Scenario Outline: Realizar compra com um item
    Given que o "<usuario>" logado com sua "<senha>" acesse a pagina de inventario
    When ele acessar o produto
    And clicar para adicionar o produto ao carrinho
    And acessar o carrinho
    And realizar o checkout fornecendo o "<nome>", "<sobrenome>" e "<cep>"
    And finalizar a compra
    Then ele será redirecionado para a tela de checkout completo

Examples:
    |usuario       |senha       |nome|sobrenome|cep|
    |standard_user |secret_sauce|Jose|silva    |123|