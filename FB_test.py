from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest

# ham login 2FA
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "C:/Users/Administrator/Downloads/Compressed/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.facebook.com")
        self.driver.maximize_window()

    def testLogin(self):
        driver = self.driver
        fbUsername = 'facebooktool01@gmail.com'
        fbPassword = 'zxczxc3##'
        auth = '6WLL AFVA GL7A R7NB LEKX 5DS5 KBLA C2VP'

        emailFieldId = "email"
        passFieldId = "pass"
        authID = "approvals_code"

        loginButtonXpath = '//button[@value="1"]'
        fbLogoXpath = '//a[contains(@href, "logo")]'
        continueXpath = '//button[@value="Tiếp tục"]'

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldId))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldId))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        authElement = driver.find_element_by_id(authID)
        # continueElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(continueXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(fbUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(fbPassword)
        loginButtonElement.click()

        authElement.clear()
        #key = getCode(auth)
        #authElement.send_keys(key)


        # continueElement.click()
        # continueElement.click()
        # WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))



    #def tearDown(self):
        #self.driver.quit()

if __name__ == '__FB_test__':
    unittest.main()
