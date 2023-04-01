from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Variável com a URL do site que iremos acessar
base_url = 'https://g1.globo.com/'


@given(u'acesso a pagina inicial do G1')
def step_impl(context):
    context.driver.get(base_url)


@when(u'clico no menu')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="header-produto"]/div[2]/div/div/div[1]/div'))).click()
    time.sleep(5)

@when(u'clico em regiões')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-1-regioes"]/a/span[1]'))).click()
    time.sleep(5)


@when(u'clico em sul')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-2-sul"]/a/span[1]'))).click()
    time.sleep(5)

@when(u'clico em parana')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-3-parana"]/a/span[1]'))).click()
    time.sleep(5)

@when(u'clico em curitiba e região')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-4-curitiba-e-regiao"]/a/span[1]'))).click()
    time.sleep(5)

@when(u'clico em paraná')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-4-curitiba-e-regiao"]/ul/button/span'))).click()
    time.sleep(5)

@when(u'clico em campos gerais e sul')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-4-campos-gerais-e-sul"]/a/span[1]'))).click()
    time.sleep(5)

@when(u'clico no icon')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-4-campos-gerais-e-sul"]/ul/button/i'))).click()
    time.sleep(5)

@when(u'clico em norte e noroeste')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-4-norte-e-noroeste"]/a/span[1]'))).click()
    time.sleep(5)

@when(u'clico em voltar')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-4-norte-e-noroeste"]/ul/button/span'))).click()
    time.sleep(5)

@when(u'clico no icon voltar')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-3-parana"]/ul/button/span'))).click()
    time.sleep(5)

@when(u'clico em rio grande do sul')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-3-rio-grande-do-sul"]/a/span[1]'))).click()
    time.sleep(5)

@when(u'clico no icon back')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-3-rio-grande-do-sul"]/ul/button'))).click()
    time.sleep(5)

@when(u'clico em santa catarina')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-3-santa-catarina"]/a/span[1]'))).click()
    time.sleep(5)


@then(u'clico em tech sc')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="menu-4-tech-sc"]/a/span[1]'))).click()
    time.sleep(5)
