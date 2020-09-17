from .sqliteHelper import SqliteHelper
from .constants import account_table_name
from .model import Account


class AccountDao:
    def __init__(self,
                 database_path):
        self.__listAccount = []
        self.database_path = database_path
        self.__sqliteHelper = SqliteHelper(self.database_path)

    @property
    def listAccount(self):
        self.__listAccount.clear()
        list = self.__sqliteHelper.select("SELECT * FROM " + account_table_name)
        for data in list:
            self.__listAccount.append(dataToAccount(data))
        return self.__listAccount

    # def getAllAccount(self):
    #     self.__listAccount = []
    #     list = self.__sqliteHelper.select("SELECT * FROM " + account_table_name)
    #     for data in list:
    #         self.__listAccount.append(dataToAccount(data))
    #     return self.__listAccount

    def addAccountObject(self, account: Account):
        self.__sqliteHelper.edit("INSERT INTO " + account_table_name + " (uid, password, code2fa, bank) "
                                        "VALUES ('" + account.uid + "', '" + account.password +
                                        "', '" + account.code2fa + "', '" + account.bank + "')")

    # Account is identified by uid, update all other columns!
    def updateAccountObject(self, account: Account):
        self.__sqliteHelper.edit("UPDATE " + account_table_name + " SET password = '" + account.password +
                                 "', code2fa = '" + account.code2fa + "', bank = '" + account.bank +
                                 "' WHERE uid = '" + account.uid + "'")

    def getAccount(self, uid):
        return dataToAccount(self.__sqliteHelper.select("SELECT * FROM " + account_table_name
                                                        + " WHERE uid = " + uid)[0])

    def addListAccount(self, listAccount: tuple):
        # listAccount: ((uid, pass, code2fa), ...)
        self.__sqliteHelper.edit("INSERT INTO " + account_table_name + " (uid, password, code2fa) "
                                                                       "VALUES " + str(listAccount)[1:-1])

    def addAccount(self, account: tuple):
        # account: ((uid, pass, code2),)
        self.__sqliteHelper.edit("INSERT INTO " + account_table_name + " (uid, password, code2fa) "
                                                                       "VALUES " + str(account)[1:-2])

    def deleteListAccount(self, listuid: tuple):
        self.__sqliteHelper.edit("DELETE FROM " + account_table_name + " WHERE uid IN " + str(listuid))

    def deleteAccount(self, uid):
        self.__sqliteHelper.edit("DELETE FROM " + account_table_name + " WHERE uid = " + uid)

    def editDB(self, query):
        self.__sqliteHelper.edit(query)

    def select(self, query):
        self.__sqliteHelper.select(query)

# Transfer data (in form of a list) to object Account
def dataToAccount(data):
    account = Account(uid=data[0], password=data[1], code2fa=data[2], bank=data[3])
    return account
