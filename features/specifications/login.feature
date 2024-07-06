Feature: Realizar login no sistema

Scenario Outline: Login válido
    Given que o usuario acessa a pagina de login
    When ele preenche seu usuário "<usuario>" e sua senha "<senha>"
    And ele aciona a opção para logar
    Then ele deve ser redirecionado para a página inicial de usuário logado

Examples:
    |usuario       |senha       |
    |standard_user |secret_sauce|

Scenario Outline: Login com senha inválida
    Given que o usuario acessa a pagina de login
    When ele preenche seu usuário "<usuario>" e a senha incorreta "<senha>"
    And ele aciona a opção para logar
    Then ele deve ser visualizar uma mensagem de usuário ou senha inválidos

Examples:
    |usuario       |senha|
    |standard_user |123  |