class Account:
    def __init__(self,
                 id_unique=-1,
                 uid="",
                 password="",
                 code2fa="",
                 ):
        self.__id_unique = id_unique
        self.__uid = uid
        self.__password = password
        self.__code2fa = code2fa

    @property
    def id_unique(self): return self.__id_unique

    @property
    def uid(self): return self.__uid

    @property
    def password(self): return self.__password

    @property
    def code2fa(self): return self.__code2fa
