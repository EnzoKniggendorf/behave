Feature: Login do usuário

  # Cenário 1: Login bem-sucedido com dados válidos
  Scenario: Usuário logado com sucesso
    Given que estou na página de login
    When insiro um email válido "usuario@teste.com" e senha "123456"
    And clico em "Entrar"
    Then devo ser redirecionado para o dashboard

  # Cenário 2: Falha no login com senha errada
  Scenario: Usuário falha ao fazer login com senha errada
    Given que estou na página de login
    When insiro um email válido "usuario@teste.com" e senha "senha_errada"
    And clico em "Entrar"
    Then devo ver a mensagem "Credenciais inválidas"

  # Cenário 3: Falha no login com email inválido
  Scenario: Usuário falha ao fazer login com email inválido
    Given que estou na página de login
    When insiro um email inválido "usuario_invalido@teste.com" e senha "123456"
    And clico em "Entrar"
    Then devo ver a mensagem "Credenciais inválidas"

  # Cenário 4: Falha no login com campos em branco
  Scenario: Usuário tenta fazer login com campos em branco
    Given que estou na página de login
    When insiro um email vazio e senha vazia
    And clico em "Entrar"
    Then devo ver a mensagem "Preencha todos os campos"

  # Cenário 5: Login bem-sucedido e logout
  Scenario: Usuário logado e realiza o logout
    Given que fiz login com sucesso
    When clico em "Sair"
    Then devo ser redirecionado para a página de login

  # Cenário 6: Tentativa de acessar o dashboard sem estar logado
  Scenario: Usuário não logado tenta acessar o dashboard
    Given que não estou logado
    When tento acessar "/dashboard"
    Then devo ser redirecionado para "/login"

  # Cenário 7: Login após falhas consecutivas
  Scenario: Usuário falha no login 3 vezes consecutivas
    Given que estou na página de login
    When falho o login 3 vezes
    Then devo ver a mensagem "Conta bloqueada após múltiplas tentativas"

  # Cenário 8: Email válido, mas sem senha
  Scenario: Usuário insere um email válido mas deixa a senha em branco
    Given que estou na página de login
    When insiro um email válido "usuario@teste.com" e deixo a senha em branco
    And clico em "Entrar"
    Then devo ver a mensagem "Senha é obrigatória"

  # Cenário 9: Recuperação de senha com email válido
  Scenario: Usuário solicita recuperação de senha
    Given que estou na página de login
    When clico em "Esqueci minha senha"
    And insiro meu email "usuario@teste.com"
    Then devo receber um email de recuperação

  # Cenário 10: Tentativa de login com email já registrado mas sem ativação de conta
  Scenario: Usuário tenta fazer login com conta não ativada
    Given que estou na página de login
    When insiro um email válido "usuario_nao_ativado@teste.com" e senha "123456"
    And clico em "Entrar"
    Then devo ver a mensagem "Conta não ativada. Verifique seu email para ativação"
