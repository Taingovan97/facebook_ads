# Process in addAccount UI


from PyQt5 import QtWidgets

from FE.AddAccount.addAccount_UI_PY import Ui_addAccount

count = 0
ds = []


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
    def getText(self, count=count):
        text = self.plainTextEditAccountText.toPlainText()
        Lines = text.splitlines()
        # Strips the newline character
        print()
        print(count)
        print()
        for line in Lines:
            print("Line {}:".format(count))
            ds.append(line.split("|"))
            ds[count].pop(len(ds[count]) - 1)
            print(ds[count])
            count += 1
        self.Dialog.close()

    # Other method

    # Show UI
    def show(self):
        self.Dialog.show()
