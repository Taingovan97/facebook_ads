from .dao import AccountDao
from .dao import Account
from .utils_BE import check_unavailable_list


class Controller:
    def __init__(self,
                 database_path="",
                 account_table_name=""):
        self.__accountDao = AccountDao(database_path=database_path, account_table_name=account_table_name)

    @property
    def listAccount(self):
        return self.__accountDao.listAccount

    def get_selected_account(self, listUid: list):
        if len(listUid) <= 0:
            return []
        elif len(listUid) == 1:
            return [self.__accountDao.getSelectedAccount(listUid[0])]
        else:
            return self.__accountDao.getSelectedListAccount(tuple(listUid))

    def login_list(self):
        pass

    def login(self,
              uid,
              password,
              code2fa,
              ):
        # login()
        pass

    def add_account(self, account: Account):
        for acc in self.listAccount:
            if acc.uid == account.uid:
                return False
        self.__accountDao.addAccountObject(account)
        return True

    def delete_account(self, uid):
        self.__accountDao.deleteAccount(uid)
        # self.__listAccount = self.__accountDao.getAllAccount()

    def update_account(self, account: Account):
        self.__accountDao.updateAccountObject(account)
        # self.__listAccount = self.__accountDao.getAllAccount()

    def add_list_account(self, listAccount: list):
        listUnavailableAcc = check_unavailable_list(listAccount=listAccount, listAvailableAccount=self.listAccount)
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
