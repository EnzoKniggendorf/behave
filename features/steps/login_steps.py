from behave import given, when, then
from splinter import Browser

@given('que estou na página de login')
def step_impl(context):
    context.browser = Browser('firefox')  # Inicializa o navegador
    context.browser.visit('http://localhost:5000/login')

@when('insiro um email válido "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    context.browser.fill('email', email)
    context.browser.fill('senha', senha)

@when('clico em "Entrar"')
def step_impl(context):
    context.browser.find_by_value('Entrar').click()

@then('devo ser redirecionado para o dashboard')
def step_impl(context):
    assert context.browser.url == 'http://localhost:5000/dashboard'

@then('devo ver a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    assert mensagem in context.browser.html
