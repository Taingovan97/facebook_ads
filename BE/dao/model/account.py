class Account:
    def __init__(self,
                 uid="",
                 name = "",
                 password="",
                 code2fa="",
                 cookie = "",
                 token = "",
                 bank="",
                 status = "",
                 ):
        self.__uid = uid
        self.__name = name
        self.__password = password
        self.__code2fa = code2fa
        self.__cookie = cookie
        self.__token = token
        self.__bank = bank
        self.__status = status

    @property
    def uid(self): return self.__uid

    @property
    def name(self): return self.__name

    @property
    def password(self): return self.__password

    @property
    def code2fa(self): return self.__code2fa

    @property
    def cookie(self): return self.__cookie

    @property
    def token(self): return self.__token

    @property
    def bank(self): return self.__bank

    @property
    def status(self): return self.__status

    @name.setter
    def name(self, value):
        self.__name = value

    @password.setter
    def password(self, value):
        self.__password = value

    @code2fa.setter
    def code2fa(self, value):
        self.__code2fa = value

    @cookie.setter
    def cookie(self, value):
        self.__cookie = value

    @token.setter
    def token(self, value):
        self.__token = value

    @bank.setter
    def bank(self, value):
        self.__bank = value

    @status.setter
    def status(self, value):
        self.__status = value
