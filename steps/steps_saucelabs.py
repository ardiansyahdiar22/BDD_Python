from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
import time


@given('Open the url saucelabs')
def openURL(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    context.driver = webdriver.Chrome("C://chromedriver_win32/chromedriver", options=options)

    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when('Type "{username}" on textfield username')
def loginProcess(context, username):
    context.driver.implicitly_wait(15)
    context.driver.find_element(By.ID, 'user-name').send_keys(username)


@when('Type "{psswd}" on textfield password')
def loginProcess2(context, psswd):
    context.driver.find_element(By.ID, 'password').send_keys(psswd)


@when('Click button login')
def clickBtnLogin(context):
    context.driver.find_element(By.ID, 'login-button').click()


@then('If login with valid username and password user successfully login, and if login with not valid email and username user can see error message')
def expectedResult(context):
    time.sleep(2)
    try:
        messageError = context.driver.find_element(By.XPATH, '//*[@data-test="error"]').text
        assert 'Epic sadface: Username and password do not match any user in this service' in messageError
    except:
        loginSuccess = context.driver.find_element(By.XPATH, '//*[@class="inventory_list"]').is_displayed()
        assert loginSuccess == True