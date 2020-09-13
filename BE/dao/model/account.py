class Account:
    def __init__(self,
                 uid="",
                 password="",
                 code2fa="",
                 bank=""
                 ):
        self.__uid = uid
        self.__password = password
        self.__code2fa = code2fa
        self.__bank = bank

    @property
    def uid(self): return self.__uid

    @property
    def password(self): return self.__password

    @property
    def code2fa(self): return self.__code2fa

    @property
    def bank(self): return self.__bank
