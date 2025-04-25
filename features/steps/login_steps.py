# features/steps/login_steps.py
from behave import given, when, then

BASE_URL = "http://localhost:5000"

@given('que estou na página de login')
def step_visit_login(context):
    context.browser.visit(f"{BASE_URL}/login")

@when('insiro um email válido "{email}" e senha "{senha}"')
def step_fill_valid(context, email, senha):
    context.browser.fill('email', email)
    context.browser.fill('senha', senha)

@when('insiro um email inválido "{email}" e senha "{senha}"')
def step_fill_invalid(context, email, senha):
    context.browser.fill('email', email)
    context.browser.fill('senha', senha)

@when('insiro um email vazio e senha vazia')
def step_fill_blank(context):
    context.browser.fill('email', '')
    context.browser.fill('senha', '')

@when('insiro um email "{email}" e deixo a senha em branco')
def step_blank_password(context, email):
    context.browser.fill('email', email)
    context.browser.fill('senha', '')

@when('clico em "Entrar"')
def step_click_enter(context):
    context.browser.find_by_value('Entrar').click()

@when('falho o login 3 vezes')
def step_fail_three_times(context):
    for _ in range(3):
        context.browser.fill('email', 'usuario@teste.com')
        context.browser.fill('senha', 'senha_errada')
        context.browser.find_by_value('Entrar').click()

@when('clico em "Esqueci minha senha"')
def step_click_forgot(context):
    context.browser.find_by_text("Esqueci minha senha").click()

@when('insiro meu email "{email}"')
def step_fill_recover_email(context, email):
    context.browser.fill('email', email)

@given('que fiz login com sucesso')
def step_logged_in(context):
    context.browser.visit(f"{BASE_URL}/login")
    context.browser.fill('email', 'usuario@teste.com')
    context.browser.fill('senha', '123456')
    context.browser.find_by_value('Entrar').click()

@when('clico em "Sair"')
def step_click_logout(context):
    context.browser.find_by_text("Sair").click()

@given('que não estou logado')
def step_not_logged(context):
    context.browser.visit(f"{BASE_URL}/logout")

@when('tento acessar "{path}"')
def step_try_access(context, path):
    context.browser.visit(f"{BASE_URL}{path}")

@then('devo ser redirecionado para "{redirect}"')
def step_check_redirect(context, redirect):
    assert redirect in context.browser.url

@then('devo ser redirecionado para o dashboard')
def step_check_dashboard(context):
    assert f"{BASE_URL}/dashboard" == context.browser.url

@then('devo ver a mensagem "{mensagem}"')
def step_check_message(context, mensagem):
    assert mensagem in context.browser.html
