from behave import given, when, then

@given('que estou na página de login')
def step_impl(context):
    context.browser.visit("http://localhost:5000/login")  # Altere a URL conforme seu app

@when('insiro um email válido "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    context.browser.fill('email', email)
    context.browser.fill('senha', senha)

@when('clico em "Entrar"')
def step_impl(context):
    context.browser.find_by_value('Entrar').click()

@then('devo ser redirecionado para o dashboard')
def step_impl(context):
    assert "/dashboard" in context.browser.url

@when('insiro um email "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    context.browser.fill('email', email)
    context.browser.fill('senha', senha)

@then('devo ver a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    assert mensagem in context.browser.html

@when('deixo o email em branco e insiro uma senha "{senha}"')
def step_impl(context, senha):
    context.browser.fill('email', '')
    context.browser.fill('senha', senha)

@when('insiro um email "{email}" e deixo a senha em branco')
def step_impl(context, email):
    context.browser.fill('email', email)
    context.browser.fill('senha', '')

@when('insiro um email inválido "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    context.browser.fill('email', email)
    context.browser.fill('senha', senha)

@when('falho o login 3 vezes')
def step_impl(context):
    for _ in range(3):
        context.browser.fill('email', 'usuario@teste.com')
        context.browser.fill('senha', 'senha_errada')
        context.browser.find_by_value('Entrar').click()

@given('que fiz login com sucesso')
def step_impl(context):
    context.browser.visit("http://localhost:5000/login")
    context.browser.fill('email', 'usuario@teste.com')
    context.browser.fill('senha', '123456')
    context.browser.find_by_value('Entrar').click()

@when('clico em "Sair"')
def step_impl(context):
    context.browser.find_by_text("Sair").click()

@then('devo ser redirecionado para a página de login')
def step_impl(context):
    assert "/login" in context.browser.url

@given('que não estou logado')
def step_impl(context):
    context.browser.visit("http://localhost:5000/logout")

@when('tento acessar "/dashboard"')
def step_impl(context):
    context.browser.visit("http://localhost:5000/dashboard")

@then('devo ser redirecionado para "/login"')
def step_impl(context):
    assert "/login" in context.browser.url

@when('clico em "Esqueci minha senha"')
def step_impl(context):
    context.browser.find_by_text("Esqueci minha senha").click()

@when('insiro meu email "{email}"')
def step_impl(context, email):
    context.browser.fill('email', email)

@then('devo receber um email de recuperação')
def step_impl(context):
    assert "Email de recuperação enviado" in context.browser.html
