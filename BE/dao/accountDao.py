from .sqliteHelper import SqliteHelper
from .model import Account
from .utils_dao import dataToAccount


class AccountDao:
    def __init__(self,
                 database_path="",
                 account_table_name=""):
        self.__listAccount = []
        self.database_path = database_path
        self.account_table_name = account_table_name
        self.__sqliteHelper = SqliteHelper(self.database_path)

    @property
    def listAccount(self):
        self.__listAccount.clear()
        listData = self.__sqliteHelper.select("SELECT * FROM " + self.account_table_name)
        for data in listData:
            self.__listAccount.append(dataToAccount(data))
        return self.__listAccount

    def getSelectedListAccount(self, listUid: tuple):
        listSelectedAccount = []
        listData = self.__sqliteHelper.select(
            "SELECT * FROM " + self.account_table_name + " WHERE uid in " + str(listUid))
        for data in listData:
            listSelectedAccount.append(dataToAccount(data))
        return listSelectedAccount

    def getSelectedAccount(self, uid):
        return dataToAccount(self.__sqliteHelper.select("SELECT * FROM " + self.account_table_name
                                                        + " WHERE uid = " + uid)[0])

    # def getAllAccount(self):
    #     self.__listAccount = []
    #     list = self.__sqliteHelper.select("SELECT * FROM " + self.account_table_name)
    #     for data in list:
    #         self.__listAccount.append(dataToAccount(data))
    #     return self.__listAccount

    def addAccountObject(self, account: Account):
        self.__sqliteHelper.edit(
            "INSERT INTO " + self.account_table_name + " (uid, password, code2fa, bank) VALUES ('" +
            account.uid + "', '" + account.password + "', '" + account.code2fa + "', '" +
            account.bank + "')")

    # Account is identified by uid, update all other columns!
    def updateAccountObject(self, account: Account):
        self.__sqliteHelper.edit("UPDATE " + self.account_table_name + " SET password = '" + account.password +
                                 "', code2fa = '" + account.code2fa + "', bank = '" + account.bank +
                                 "' WHERE uid = '" + account.uid + "'")

    def addListAccount(self, listAccount: tuple):
        # listAccount: ((uid, pass, code2fa), ...)
        self.__sqliteHelper.edit("INSERT INTO " + self.account_table_name + " (uid, password, code2fa) "
                                                                            "VALUES " + str(listAccount)[1:-1])

    def addAccount(self, account: tuple):
        # account: ((uid, pass, code2),)
        self.__sqliteHelper.edit("INSERT INTO " + self.account_table_name + " (uid, password, code2fa) "
                                                                            "VALUES " + str(account)[1:-2])

    def deleteListAccount(self, listuid: tuple):
        self.__sqliteHelper.edit("DELETE FROM " + self.account_table_name + " WHERE uid IN " + str(listuid))

    def deleteAccount(self, uid):
        self.__sqliteHelper.edit("DELETE FROM " + self.account_table_name + " WHERE uid = " + uid)

    def editDB(self, query):
        self.__sqliteHelper.edit(query)

    def select(self, query):
        self.__sqliteHelper.select(query)
