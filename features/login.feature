Feature: Login do usuário

  Scenario: Usuário logado com sucesso
    Given que estou na página de login
    When insiro um email válido "usuario@teste.com" e senha "123456"
    And clico em "Entrar"
    Then devo ser redirecionado para o dashboard

  Scenario: Usuário falha ao fazer login com senha errada
    Given que estou na página de login
    When insiro um email válido "usuario@teste.com" e senha "senha_errada"
    And clico em "Entrar"
    Then devo ver a mensagem "Credenciais inválidas"

  # Outras cenas...
