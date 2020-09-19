import requests
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def getUrl(idFriend):
    url = "https://d.facebook.com/a/mobile/friends/profile_add_friend.php?subjectid=" +idFriend+ "&istimeline=1&hf=profile_button&fref=pymk&frefid=7&referrer_uri=https%3A%2F%2Fd.facebook.com%2Fhome.php%3Fref_component%3Dmbasic_home_header%26ref_page%3D%252Fwap%252Fprofile_timeline.php%253Afriends%26refid%3D17&gfid=AQAqon8862MM1KdM"
    return url

def getHeader(idFriend, str):
    headers = {
        'authority': 'd.facebook.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.facebook.com/profile.php?id=' + idFriend,
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8,fr;q=0.7',
        'cookie': str
    }
    return headers

# def addFriend(idFriend, cookie):
#     re = requests.request("GET", url=getUrl(idFriend), headers=getHeader(idFriend,cookie))
#     return re

def addFriend(driver, idfriend):
    driver.get('https://www.facebook.com/profile.php?id=' +idfriend)
    buttonPath = '//button[contains(@aria-label, "as a friend")]'
    element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(buttonPath))
    actions = ActionChains(driver)
    actions.click(element)
    actions.perform()

    return driver
