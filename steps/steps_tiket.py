from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
import time

@given('Open url tiket.com')
def openURL(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    context.driver = webdriver.Chrome("C://chromedriver_win32/chromedriver", options=options)

    context.driver.maximize_window()
    context.driver.get("https://www.tiket.com/kereta-api")


@when('User choose hometown and destination and user chooses how many passengers')
def steps1(context):
    context.driver.implicitly_wait(15)
    context.driver.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div').click()
    context.driver.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[2]/div[2]/div[1]').click()

    context.driver.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[3]/div[2]/div[2]/div').click()
    context.driver.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[3]/div[2]/div[2]/div/div/div[2]/ul/li[1]/div[2]/div[1]').click()
    context.driver.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]/div').click()    
    context.driver.find_element(By.XPATH, '//*[@class="tix tix-cancel icon-close"]').click()    

@when('User click button search ticket')
def steps2(context):
    context.driver.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[4]/button').click()


@then('User can see list available trains')
def steps3(context):
    time.sleep(2)
    ticketList = context.driver.find_element(By.XPATH, '//*[@class="train-list"]').is_displayed()
    assert ticketList == True