from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Variável com a URL do site que iremos acessar
base_url = 'https://g1.globo.com/sc/santa-catarina/techsc/'


@given(u'acesso a pagina tech sc')
def step_impl(context):
    context.driver.get(base_url)

@then(u'clico no header santa catarina')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="header-produto"]/div[2]/div/div/h1/div/a[1]'))).click()
    time.sleep(5)

def after_scenario(context, scenario):
    driver.quit()