from BE.dao import Account
from ..api_login_dFace import login
from ..api_addFr import addFriend
from ..api_accept_friend import acceptFr

"""
return 1: active sucessful

return 2: active fail
"""
class facebook:
    def __init__(self,
                 acc: Account,
                 driver=None):
        self.acc = acc
        self.driver = driver

    def setCookie(self, cookie):
        self.acc.cookie = cookie

    def login(self):
        self.driver, self.acc.cookie = login(self.acc.uid, self.acc.password, self.acc.code2fa)
        if (self.driver is None):
            return 2
        else:
            return 1

    def addFriend(self, idFriend):
        self.driver = addFriend(self.driver, idFriend)


    def acceptFriend(self):
        self.driver = acceptFr(self.driver)
