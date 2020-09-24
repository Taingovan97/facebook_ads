from selenium.webdriver.common.by import By
def acceptFr(driver):
    confirmPath = '//a[contains(@href, "/a/notifications.php?confirm=")]'
    while len(driver.find_elements(By.XPATH, confirmPath))> 0:
        confirmElement = driver.find_element_by_xpath(confirmPath)
        confirmElement.click()
    return driver