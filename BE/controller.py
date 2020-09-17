# from .core import login
from .dao import AccountDao
from .dao import Account
from .constants import DATABASE_PATH


class Controller:
    def __init__(self):
        # self.__accountDao = AccountDao(database_path=DATABASE_PATH)
        self.__accountDao = AccountDao(database_path=DATABASE_PATH)

    @property
    def listAccount(self):
        return self.__accountDao.listAccount

    def login(self,
              uid,
              password,
              code2fa,
              ):
        # login(fbUsername=uid, fbPassword=password,code_2fa=code2fa)
        pass

    # def get_all_account(self):
    #     # self.__listAccount = self.__accountDao.getAllAccount()
    #     return self.__listAccount

    def add_account(self, account: Account):
        for acc in self.listAccount:
            if acc.uid == account.uid:
                return False
        self.__accountDao.addAccount(account)
        return True

    def delete_account(self, uid):
        self.__accountDao.deleteAccount(uid)
        # self.__listAccount = self.__accountDao.getAllAccount()

    def update_account(self, account: Account):
        self.__accountDao.updateAccount(account)
        # self.__listAccount = self.__accountDao.getAllAccount()

    def add_list_account(self, listAccount: list):
        listUnavailableAcc = []
        # listAccount will be [[uid, pass, code2fa],...]
        for acc in listAccount:
            listUnavailableAcc.append(tuple(acc))
            if len(self.listAccount) != 0:
                for acc_available in self.listAccount:
                    if acc_available.uid == acc[0]:
                        listUnavailableAcc.remove(tuple(acc))
                        break
        listUnavailableAcc = tuple(listUnavailableAcc)
        if len(listUnavailableAcc) == 0:
            pass
        elif len(listUnavailableAcc) == 1:
            self.__accountDao.addAccount(listUnavailableAcc)
        else:
            self.__accountDao.addListAccount(listUnavailableAcc)
        return len(listUnavailableAcc)


    def delete_list_account(self, listuid: list):
        if len(listuid) == 1:
            self.__accountDao.deleteAccount(listuid[0])
        else:
            self.__accountDao.deleteListAccount(tuple(listuid))
