from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
import time

@given('Open the shop URL')
def openTheURL(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    context.driver = webdriver.Chrome("C://chromedriver_win32/chromedriver", options=options)

    context.driver.maximize_window()
    context.driver.get("https://www.tokopedia.com/unilever")


@when('Search a product name and click search')
def searchProduct(context):
    context.driver.implicitly_wait(15)
    context.driver.find_element(By.XPATH, '//*[@class="css-1wc186l e110g5pc0"]').send_keys('ponds')
    context.driver.find_element(By.XPATH, '//*[@class="css-1czin5k e1v32nag1"]').click()


@when('Click product card and choose share with copy link product')
def actionProduct(context):
    context.driver.find_element(By.XPATH, '//*[@data-testid="master-product-card"]').click()
    context.driver.find_element(By.XPATH, '//*[@data-testid="pdpShareButton"]').click()
    context.driver.find_element(By.XPATH, '//*[@data-testid="btnCopyShare"]').click()


@then('User can see toaster message if success copy link product')
def successToaster(context):
    time.sleep(2)
    toaster = context.driver.find_element(By.XPATH, '//P[@class="css-jtcihq-unf-heading e1qvo2ff8"]').text
    assert 'Tautan berhasil di salin' in toaster