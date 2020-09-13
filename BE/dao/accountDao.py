from .sqliteHelper import SqliteHelper
from .constants import account_table_name
from .model import Account


class AccountDao:
    def __init__(self):
        self.__sqliteHelper = SqliteHelper()

    def getAllAccount(self):
        listAccount = []
        list = self.__sqliteHelper.select("SELECT * FROM " + account_table_name)
        for data in list:
            listAccount.append(dataToAccount(data))
        return listAccount

    def addAccount(self, account: Account):
        return self.__sqliteHelper.edit("INSERT INTO " + account_table_name + " (uid, password, code2fa, bank) "
                                        "VALUES ('" + account.uid + "', '" + account.password +
                                        "', '" + account.code2fa + "', '" + account.bank + "')")

    def deleteAccount(self, uid):
        return self.__sqliteHelper.edit("DELETE FROM " + account_table_name + " WHERE uid = " + uid)

    # Account is identified by uid, update all other columns!
    def updateAccount(self, account: Account):
        self.__sqliteHelper.edit("UPDATE " + account_table_name + " SET password = '" + account.password +
                                 "', code2fa = '" + account.code2fa + "', bank = '" + account.bank +
                                 "' WHERE uid = '" + account.uid + "'")

    def getAccount(self, uid):
        return dataToAccount(self.__sqliteHelper.select("SELECT * FROM " + account_table_name
                                                        + " WHERE uid = " + uid)[0])

    def editDB(self, query):
        self.__sqliteHelper.edit(query)

    def select(self, query):
        self.__sqliteHelper.select(query)

# Transfer data (in form of a list) to object Account
def dataToAccount(data):
    account = Account(uid=data[0], password=data[1], code2fa=data[2], bank=data[3])
    return account
