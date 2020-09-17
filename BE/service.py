from typing import List

from .controller import Controller
from .dao import Account


class Service:
    def __init__(self):
        self.__controller = Controller()
        # self.listAccount = []

    def get_table(self):
        # listAccount = []
        # for account in self.controller.get_all_account():
        #     acc = [account.uid, account.name, account.password, account.code2fa, account.cookie,
        #            account.token, account.bank, account.status]
        #     listAccount.append(acc)
        return self.__controller.listAccount

    def add_account(self, account: list):
        accountModel = Account(uid=account[0], password=account[1], code2fa=account[2])
        return self.__controller.add_account(accountModel)

    def delete_account(self, uid: str):
        self.__controller.delete_account(uid)

    def update_account(self, account: list):
        accountModel = Account(uid=account[0], name=account[1], password=account[2], code2fa=account[3],
                               cookie=account[4], token=account[5], bank=account[6], status=account[7])
        self.__controller.update_account(accountModel)

    def add_list_account(self, listAccount: list):
        # listAccount will be [[uid, pass, code2fa],...]
        return self.__controller.add_list_account(listAccount)

    def delete_list_account(self, listuid: list):
        self.__controller.delete_list_account(listuid)
