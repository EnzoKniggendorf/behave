# language: pt
Funcionalidade: Testar sistema de login

  Cenário: Login com credenciais válidas
    Dado que estou na página de login
    Quando insiro um email válido "usuario@teste.com" e senha "123456"
    E clico em "Entrar"
    Então devo ser redirecionado para o dashboard

  Cenário: Login com senha incorreta
    Dado que estou na página de login
    Quando insiro um email válido "usuario@teste.com" e senha "errada"
    E clico em "Entrar"
    Então devo ver a mensagem "Senha incorreta"

  Cenário: Login com email não cadastrado
    Dado que estou na página de login
    Quando insiro um email "naoexiste@teste.com" e senha "123456"
    E clico em "Entrar"
    Então devo ver a mensagem "Email não cadastrado"

  Cenário: Login com email em branco
    Dado que estou na página de login
    Quando deixo o email em branco e insiro uma senha "123456"
    E clico em "Entrar"
    Então devo ver a mensagem "Email é obrigatório"

  Cenário: Login com senha em branco
    Dado que estou na página de login
    Quando insiro um email "usuario@teste.com" e deixo a senha em branco
    E clico em "Entrar"
    Então devo ver a mensagem "Senha é obrigatória"

  Cenário: Login com email inválido (sem @)
    Dado que estou na página de login
    Quando insiro um email "usuario.teste.com" e senha "123456"
    E clico em "Entrar"
    Então devo ver a mensagem "Email inválido"

  Cenário: Tentativa de login após 3 falhas
    Dado que estou na página de login
    Quando falho o login 3 vezes
    Então minha conta deve ser bloqueada temporariamente

  Cenário: Recuperação de senha
    Dado que estou na página de login
    Quando clico em "Esqueci minha senha"
    E insiro meu email "usuario@teste.com"
    Então devo receber um email de recuperação

  Cenário: Logout após login bem-sucedido
    Dado que fiz login com sucesso
    Quando clico em "Sair"
    Então devo ser redirecionado para a página de login

  Cenário: Acesso a página restrita sem login
    Dado que não estou logado
    Quando tento acessar "/dashboard"
    Então devo ser redirecionado para "/login"
