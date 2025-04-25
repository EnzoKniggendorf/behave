from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from behave import use_fixture

# Função para configurar o WebDriver
def setup_driver(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Rodar no modo headless (sem interface gráfica)
    chrome_options.add_argument('--disable-gpu')  # Desabilitar GPU (para servidores sem suporte a gráficos)
    chrome_options.add_argument('--no-sandbox')  # Necessário para rodar em alguns ambientes CI (como GitHub Actions)

    # Inicializando o WebDriver com o ChromeDriver
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Função para parar o WebDriver
def teardown_driver(context):
    context.driver.quit()

# Usando o fixture para configurar e finalizar o WebDriver
def before_all(context):
    setup_driver(context)

def after_all(context):
    teardown_driver(context)

