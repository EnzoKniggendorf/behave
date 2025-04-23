# features/steps/login_steps.py
from behave import *

@given('que estou na página de login')
def step_impl(context):
    context.browser.visit('/login')  # Exemplo com Selenium

@when('insiro um email válido "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    context.browser.fill('email', email)
    context.browser.fill('senha', senha)

@when('clico em "{botao}"')
def step_impl(context, botao):
    context.browser.find_by_text(botao).click()

@then('devo ser redirecionado para o dashboard')
def step_impl(context):
    assert context.browser.is_text_present('Bem-vindo ao Dashboard')

@then('devo ver a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    assert context.browser.is_text_present(mensagem)