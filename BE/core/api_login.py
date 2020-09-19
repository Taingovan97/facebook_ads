from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import requests
from BE.core import auth, constants
import time

def login(fbUsername, fbPassword, code_2fa = None):
    driver = webdriver.Chrome(executable_path=constants.CHROME_PATH)
    driver.get("https://www.facebook.com")

    emailFieldId = "email"
    passFieldId = "pass"
    authID = "approvals_code"

    loginButtonXpath = '//button[@value="1"]'
    fbLogoXpath = '//a[contains(@href, "logo")]'

    # trường username, password và login
    emailFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(emailFieldId))
    passFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(passFieldId))
    loginButtonElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))


    # điển tên đăng nhập
    emailFieldElement.clear()
    emailFieldElement.send_keys(fbUsername)
    # điền password
    passFieldElement.clear()
    passFieldElement.send_keys(fbPassword)
    # click đăng nhập
    loginButtonElement.click()
    if (code_2fa!= None):
        # trường mã xác thực
        authElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(authID))
        key = auth.get_code_2fa(code_2fa)
        print(key)
        # nhập key xác thực
        authElement.send_keys(key)

        continueXpath = '//button[@value="Tiếp tục"]'
        continueElement = driver.find_element_by_xpath(continueXpath)
        continueElement.click()

        driver.find_elements()
        while len(driver.find_elements(By.XPATH, continueXpath)) > 0:
            continueElement = driver.find_element_by_xpath(continueXpath)
            continueElement.click()

    time.sleep(3)
    # get cookie
    temp = driver.get_cookies()
    cookie = ''
    for i in temp:
        cookie += i['name'] + '=' + i['value'] + ';' + ''

    return driver, cookie


