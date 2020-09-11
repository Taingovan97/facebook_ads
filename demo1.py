import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import constants
import requests

id = '100005188112837'
id1 = '100050911668510'
def login(fbUsername, fbPassword, acc = None):
    driver = webdriver.Chrome(executable_path=constants.CHROME_PATH)
    driver.get("https://www.facebook.com")



    emailFieldId = "email"
    passFieldId = "pass"
    #authID = "approvals_code"

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

    # # trường mã xác thực
    # authElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(authID))
    # authElement.clear()
    # key = auth.get_code_2fa(code_2fa)
    # print(key)
    # # nhập key xác thực
    # authElement.send_keys(key)

    # continueXpath = '//button[@value="Tiếp tục"]'
    # continueElement = driver.find_element_by_xpath(continueXpath)
    # continueElement.click()

    # driver.find_elements()
    # while len(driver.find_elements(By.XPATH, continueXpath)) > 0:
    #     continueElement = driver.find_element_by_xpath(continueXpath)
    #     continueElement.click()



    str = ''
    for cookie in driver.get_cookies():
        str+= cookie['name'] + '=' + cookie['value'] + ';' + ''


    # if (acc != None):
    #     driver.get("https://www.facebook.com/"+acc)

    #print(str)
    url = "https://www.facebook.com/ajax/add_friend/action/?to_friend=" + id + "&action=add_friend&how_found=profile_button&ref_param=unknown&link_data[gt][type]=xtracking&link_data[gt][xt]=48.%7B%22event%22%3A%22add_friend%22%2C%22intent_status%22%3Anull%2C%22intent_type%22%3Anull%2C%22profile_id%22%3A100007481102571%2C%22ref%22%3A1%7D&link_data[gt][profile_owner]=100007481102571&link_data[gt][ref]=timeline%3Atimeline&logging_location=&http_referer=https%3A%2F%2Fwww.facebook.com%2F%3Fref%3Dtn_tnmn&floc=profile_button&frefs[0]=unknown"
    headers = {
        'authority': 'www.facebook.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'viewport-width': '710',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://www.facebook.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.facebook.com/?id=' + id,
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8,fr;q=0.7',
        'cookie': str
    }
    payload = '__user='+ id1+'&__a=1&__dyn=7AgNeS4amaWxd2u6aJGi9FxqeCwKAKGgmAGt94WpEbE9ES2N6xCaxubwTwyCwVBDyubnyorxuF98ScDKaxeUPwExaawCx138S2SQh6UXU9468Oajz8gCxm3i5VokKeyEqx66Ecolm26q499oeGzUWeCxy1hzFVk3K6UowJxCWxS68nBy8pK44WwTgCmfx-byEkyob-1dx3xiGzXAxeQm3a4ogzd29pUiAUG2HQ7FbBojUC6po-fz8Cm4U9898GfxnCxi7Wz8GEcE-h2EgVFXAy8aElxeaKE-3m4rybCzogy898e8Wqexp2UtGi9zEO2-by8ix22mbwgUuG15xmE9EjwgEiK8xi8BwBzUuwFABwkUjxy224Umwso88co9oy5olxa2m4UcUSUjwhE&__csr=&__req=bh&__beoa=0&__pc=PHASED%3ADEFAULT&dpr=1&__ccg=EXCELLENT&__rev=1002636893&__s=0gddvj%3Atoxfuv%3A74i0ia&__hsi=6870840823560647435-0&__comet_req=0&fb_dtsg=AQGMpYl37ZuY%3AAQFBnJ7M4FMs&jazoest=21975&__spin_r=1002636893&__spin_b=trunk&__spin_t=1599677290'
    requests.request("POST", url= url, headers = headers, data=payload)

    return driver

user = '0346377012'
pa = 'tai@28293839'
login(user, pa)