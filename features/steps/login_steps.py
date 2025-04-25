from behave import given, when, then

@given('que estou na página de login')
def step_impl(context):
    # Aqui, você deve adicionar o código para navegar até a página de login.
    pass

@when('insiro um email válido "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    # Aqui, insira o código para preencher o formulário de login.
    pass

@when('clico em "Entrar"')
def step_impl(context):
    # Código para clicar no botão "Entrar".
    pass

@then('devo ser redirecionado para o dashboard')
def step_impl(context):
    # Verifique se o redirecionamento foi para o dashboard.
    pass

@then('devo ver a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    # Verifique se a mensagem esperada aparece na tela.
    pass
