Feature: Adicionar produtos ao carrinho

Scenario Outline: Adicionar um produto ao carrinho e validar
    Given que o "<usuario>" logado com sua "<senha>" acesse a pagina de inventario
    When ele acessar o produto
    And clicar para adicionar o produto ao carrinho
    Then ele deve ver o icone indicando presença de produto no carinho

Examples:
    |usuario       |senha       |
    |standard_user |secret_sauce|