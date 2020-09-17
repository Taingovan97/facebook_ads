# Process in addAccount UI


from PyQt5 import QtWidgets, QtCore

from FE.AddAccount.addAccount_UI_PY import Ui_addAccount
from FE.window import Window


class AddAccount(Ui_addAccount, Window):
    def __init__(self, modal=True):
        super().__init__()
        self.modal = modal

        # Add setup Add account UI
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setModal(self.modal)
        self.setupUi(self.Dialog)
        self.Dialog.setFixedSize(600, 400)

        # Connect signals
        self.buttonAdd.clicked.connect(self.getText)

    # Connect signals method
    def getText(self):
        listTotalAcc = []
        text = self.plainTextEditAccountText.toPlainText()
        Lines = text.splitlines()

        for line in Lines:
            acc = line.split("|")
            for ele in acc.copy():
                if ele == "":
                    acc.remove(ele)
            if len(acc) == 3:
                # Acc will be [uid, pass, code2fa]
                listTotalAcc.append(acc)
                # addedCheck = self._service.add_account(acc)
                # if addedCheck:
                #     addedCount += 1
        addedCount = self._service.add_list_account(listTotalAcc)

        self.label_3.setText(QtCore.QCoreApplication.translate("addAccount", "Lưu ý: Chọn đúng định dạng trước khi thêm"
                                                                             "\nUID của các tài khoản phải khác nhau"
                                                                             "\nĐã thêm " + str(addedCount) + "/" + str(
                                                                                len(listTotalAcc))))
        self.signal.emit("ShowTable")

    # Other method

    # Show UI
    def show(self):
        self.Dialog.show()
