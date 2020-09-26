from .controller import Controller
from .dao import Account
from constants import DATABASE_PATH, account_table_name


class Service:
    __controller = Controller(DATABASE_PATH, account_table_name)

    """Start table service"""
    def get_full_table(self):
        return Service.__controller.listAccount

    def get_seleted_table(self, listUid: list):
        listAccount = Service.__controller.get_selected_account(listUid)
        if len(listUid) > len(listAccount):
            print("Co tai khoan khong ton tai trong co so du lieu!")
        return listAccount

    def add_account(self, account: list):
        accountModel = Account(uid=account[0], password=account[1], code2fa=account[2])
        return Service.__controller.add_account(accountModel)

    def delete_account(self, uid: str):
        Service.__controller.delete_account(uid)

    def update_account(self, account: list):
        accountModel = Account(uid=account[0], name=account[1], password=account[2], code2fa=account[3],
                               cookie=account[4], token=account[5], bank=account[6], status=account[7])
        Service.__controller.update_account(accountModel)

    def add_list_account(self, listAccount: list):
        # listAccount will be [[uid, pass, code2fa],...]
        return Service.__controller.add_list_account(listAccount)

    def delete_list_account(self, listUid: list):
        Service.__controller.delete_list_account(listUid)
    """End table service"""

    """Start Main Window service"""
    def login(self, listUid: list):
        self.__controller.login(list)

    """Start Add Via service"""
    def add_via(self):
        return
    """End Via service"""
