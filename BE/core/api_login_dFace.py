from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# import requests
from BE.core import auth, constants
import time

def login(fbUsername, fbPassword, code_2fa = None):
    driver = webdriver.Chrome(executable_path=constants.CHROME_PATH)
    driver.get("https://mbasic.facebook.com")

    d_email = "m_login_email"
    d_passname = "pass"
    authID = "approvals_code"

    d_login = '//input[@name="login"]'

    # trường username, password và login
    emailFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(d_email))
    passFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_name(d_passname))
    loginButtonElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_xpath(d_login))

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

        d_send = '//input[@name="submit[Submit Code]"]'
        sendElement = driver.find_element_by_xpath(d_send)
        sendElement.click()

        d_continue = '//input[@name="submit[Continue]"]'
        driver.find_elements()
        while len(driver.find_elements(By.XPATH, d_continue)) > 0:
            continueElement = driver.find_element_by_xpath(d_continue)
            continueElement.click()

    time.sleep(3)
    # get cookie
    temp = driver.get_cookies()
    cookie = ''
    for i in temp:
        cookie += i['name'] + '=' + i['value'] + ';' + ''

    return driver, cookie


