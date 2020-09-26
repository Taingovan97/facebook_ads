# Process in addAccount UI

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QCoreApplication

from FE.AddAccount.addAccount_UI_PY import Ui_AddAccount
from FE.windowSignal import WindowSignal


class AddAccount(Ui_AddAccount, WindowSignal):

    def __init__(self, modal=True):
        super().__init__()
        self.modal = modal

        # Add setup Add account UI
        self.Dialog = QDialog()
        self.Dialog.setModal(self.modal)
        self.setupUi(self.Dialog)
        self.Dialog.setFixedSize(600, 400)
        self.label_3.setText(QCoreApplication.translate("addAccount",
                                                        "Lưu ý:\tChọn đúng định dạng trước khi thêm\n"
                                                        "\tUID của các tài khoản phải khác nhau\n"
                                                        ))

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
        number_of_valid_acc = len(listTotalAcc)
        if 0 == number_of_valid_acc:
            self.label_3.setText(QCoreApplication.translate("addAccount",
                                                            "Lưu ý:\tChọn đúng định dạng trước khi thêm\n"
                                                            "\tUID của các tài khoản phải khác nhau\n"
                                                            "\tKhông có tài khoản nào hợp lệ"))
        else:
            addedCount = WindowSignal._service.add_list_account(listTotalAcc)

            self.label_3.setText(QCoreApplication.translate("addAccount",
                                                            "Lưu ý:\tChọn đúng định dạng trước khi thêm\n"
                                                            "\tUID của các tài khoản phải khác nhau\n"
                                                            "\tĐã thêm " + str(addedCount) + "/" +
                                                            str(number_of_valid_acc)))
            self.signal.emit("ShowTable")

    # Other method

    # Show UI
    def show(self):
        self.Dialog.show()
