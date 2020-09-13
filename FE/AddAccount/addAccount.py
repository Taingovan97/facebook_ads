# Process in addAccount UI


from PyQt5 import QtWidgets

from FE.AddAccount.addAccount_UI_PY import Ui_addAccount


class AddAccount(Ui_addAccount):
    def __init__(self,
                 modal=True,
                 ):
        # Setup Add account UI
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setModal(modal)
        self.setupUi(self.Dialog)

        # Connect signals
        self.buttonAdd.clicked.connect(self.getText)

    # Connect signals method
    def getText(self):
        text = self.plainTextEditAccountText.toPlainText()
        Lines = text.splitlines()
        # Strips the newline character
        print()
        print()
        for index, line in enumerate(Lines):
            print(f"Line {index}:")
            acc = line.split("|")
            acc.pop()
            print(acc)
        self.Dialog.close()

    # Other method

    # Show UI
    def show(self):
        self.Dialog.show()
