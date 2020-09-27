from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def addFriend(driver, idfriend):
    driver.get('https://mbasic.facebook.com/' +idfriend)

    buttonPath = '//a[contains(@href,"profile_add_friend.php?subjectid=")]'
    try:
        element = driver.find_element_by_xpath(buttonPath)
        element.click()
    except:
        return 0
    return driver
