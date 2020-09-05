import unittest

from git_project import takeAuth
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



# ham login 2FA
class LoginTest(unittest.TestCase):
    # khoi tao driver browser
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "C:/Users/Administrator/Downloads/Compressed/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.facebook.com")
        #self.driver.maximize_window()

    # login
    def testLogin(self):
        driver = self.driver
        fbUsername = 'facebooktool01@gmail.com'
        fbPassword = 'zxczxc3##'
        auth = 'KHKW SCQV 6CMO H2GM VCTP VGYI RDIP 5BHT'        # ma 2FA


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
        #authElement.clear()
        key = takeAuth.getCode(auth)
        # nhập key xác thực
        authElement.send_keys(key)

        continueXpath = '//button[@value="Tiếp tục"]'
        continueElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(continueXpath))
        continueElement.click()
        # while continueElement in driver.page_source:
        #     continueElement.click()
        #WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

        # trường 'lưu'
        savePath = '//input[@id="u_0_2"]'
        saveElement = driver.find_element_by_xpath(savePath)
        continueElement2 = driver.find_element_by_xpath(continueXpath)

        saveElement.click()
        continueElement2.click()


    # def tearDown(self):
    #     self.driver.quit()

if __name__ == '__FB_test__':
    unittest.main()
