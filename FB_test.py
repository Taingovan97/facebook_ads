from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest



# def getCode(code):
#     dr = webdriver.Chrome(executable_path="C:/Users/Administrator/Downloads/Compressed/chromedriver_win32/chromedriver.exe")
#     dr.get("https://gauth.apps.gbraad.nl/")
#
#     editButtonPath = '//a[@id="edit"]'
#     addButtonPath = '//a[@id="addButton"]'
#     addKeyPath = '//a[@id="addKeyButton"]'
#     path = '//li[contains(@class, "ui-li-static ui-body-inherit ui-last-child")]'
#
#     editElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_xpath(editButtonPath))
#     addElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_xpath(addButtonPath))
#     accountElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_id('keyAccount'))
#     keyElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_id('keySecret'))
#     addKeyElement = WebDriverWait(dr, 5).until(lambda dr: dr.find_element_by_xpath(addKeyPath))
#
#     editElement.click()
#     addElement.click()
#     accountElement.clear()
#     accountElement.send_keys('abcd')
#     keyElement.clear()
#     keyElement.send_keys(code)
#     addKeyElement.click()
#
#     #lay ma xac thuc
#     num = dr.find_element_by_xpath(path).find_element_by_tag_name('h3').text
#     dr.quit()
#
#     return num


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "C:/Users/Administrator/Downloads/Compressed/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.facebook.com")
        self.driver.maximize_window()

    def testLogin(self):
        driver = self.driver
        fbUsername = '0346377012'
        fbPassword = 'tai@28293839'
        auth = 'O5GZ S2XB WOY3 NA2M WM4T QGQQ 7VYO 53CB'

        emailFieldId = 'email'
        passFieldId = 'pass'
        authID = 'approvals_code'

        loginButtonXpath = '//button[@id="u_0_b"]'
        fbLogoXpath = '//a[contains(@href, "logo")]'
        continueXpath = '//button[@value="Tiếp tục"]'

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldId))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldId))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        authElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(authID))
        # continueElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(continueXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(fbUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(fbPassword)
        loginButtonElement.click()

        authElement.clear()

        #authElement.send_keys(getCode(auth))

        #authElement.send_keys(getCode(auth))

        # continueElement.click()
        # continueElement.click()
        # WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))



    #def tearDown(self):
        #self.driver.quit()

if __name__ == '__FB_test__':
    unittest.main()
