from BE.dao import Account


class fb:
    def __init__(self,
                 acc: Account,
                 driver=None):
        self.acc = acc
        self.driver = driver

    def setCookie(self, cookie):
        self.acc.cookie = cookie

    def login(self):
        self.driver, self.acc.cookie = login()

    def addfriend(self):
        addfriend(self.driver)
        self.driver = driver
