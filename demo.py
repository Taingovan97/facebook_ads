from BE import constants
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import auth


def addPayment(fbUsername, fbPassword, code_2fa, fbUID):
    driver = webdriver.Chrome(constants.CHROME_PATH)
    driver.get("https://wwww.facebook.com/ads/manager/account_settings/account_billing/?act="+fbUID+"&pid=p1&page=account_settings&tab=account_billing_settings")

    # log in nhu fb thong thuong
    # dropDownId = 'userNavigationLabel'
    # dropDownEle = driver.find_element_by_id(dropDownId)
    # dropDownEle.click()

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



id = '3732475760114916'
