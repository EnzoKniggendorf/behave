# features/environment.py
from splinter import Browser

def before_all(context):
    # sempre headless no CI
    context.browser = Browser('firefox', headless=True)

def after_all(context):
    context.browser.quit()