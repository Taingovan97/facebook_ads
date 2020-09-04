

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def getCode(code):
    dr = webdriver.Chrome(executable_path="C:/Users/Administrator/Downloads/Compressed/chromedriver_win32/chromedriver.exe")
    dr.get("https://gauth.apps.gbraad.nl/")

    editButtonPath = '//a[@id="edit"]'
    addButtonPath = '//a[@id="addButton"]'
    addKeyPath = '//a[@id="addKeyButton"]'
    path = '//li[contains(@class, "ui-li-static ui-body-inherit ui-last-child")]'

    editElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_xpath(editButtonPath))
    addElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_xpath(addButtonPath))
    accountElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_id('keyAccount'))
    keyElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_id('keySecret'))
    addKeyElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_xpath(addKeyPath))

    editElement.click()
    addElement.click()
    accountElement.clear()
    accountElement.send_keys('abcd')
    keyElement.clear()
    keyElement.send_keys(code)
    addKeyElement.click()

    #lay ma xac thuc
    num = dr.find_element_by_xpath(path).find_element_by_tag_name('h3').text
    dr.quit()

    return num
# code = '6WLL AFVA GL7A R7NB LEKX 5DS5 KBLA C2VP'
# print(getCode(code))
