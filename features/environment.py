from selenium import webdriver

def before_all(context):
    # Aqui você pode inicializar o driver do navegador (usando, por exemplo, o Chrome ou Firefox).
    context.driver = webdriver.Firefox()

def after_all(context):
    # Fechar o navegador após todos os testes
    context.driver.quit()
