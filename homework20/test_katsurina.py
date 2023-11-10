from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_actions import WheelActions
from selenium.webdriver.common.action_chains import ActionChains

import time
def test_serch():
    driver = Chrome()
    driver.get('https://ua.katsurina.com/')
    driver.maximize_window()
    time.sleep(3)
    serch_locator = '//a[@href="/search"]'
    serch = driver.find_element('xpath',serch_locator)
    serch.click()
    field_Locator = '//div[@class="form-group form-group--line"]//input[@class="form-control"]'
    element = driver.find_element(by='xpath', value=field_Locator)
    time.sleep(2)
    element.send_keys('Сорочка')
    element.send_keys(Keys.ENTER)
    time.sleep(5)

def test_cart():
    driver = Chrome()
    driver.get('https://ua.katsurina.com/')
    driver.maximize_window()
    time.sleep(3)
    cart_locator = '//li/a[@href="/cart"]'
    cart = driver.find_element('xpath',cart_locator)
    cart.click()
    time.sleep(5)
def test_gift():
    driver = Chrome()
    driver.get('https://ua.katsurina.com/')
    time.sleep(3)
    gift_locator = '//a[@href="/collections/gift-card"][1]'
    gift = driver.find_element('xpath', gift_locator)
    gift.click()
    time.sleep(5)

def test_womanclick_dressclick():
    driver = Chrome()
    driver.get('https://ua.katsurina.com/')
    driver.maximize_window()
    time.sleep(2)
    woman_locator ='//div[@class ="header-nav__primary-wrap"]//a[ @ href="/collections/woman"][1]'
    woman = driver.find_element('xpath', woman_locator)
    woman.click()
    dress_locator = '//div[@class="child-list"]//a[@href="/collections/dress"]'
    dress = driver.find_element('xpath', dress_locator)
    dress.click()
    time.sleep(5)

def test_new():
    driver = Chrome()
    driver.get('https://ua.katsurina.com/')
    driver.maximize_window()
    time.sleep(2)
    new_locator = "//ul[@class='header-nav__primary hide-xs hide-sm']//a[@href='/collections/new']"
    new = driver.find_element('xpath', new_locator)
    new.click()
    time.sleep(5)