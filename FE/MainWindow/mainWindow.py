# Process in mainwindow UI


from PyQt5 import QtWidgets

from FE.MainWindow.mainWindow_UI_PY import Ui_MainWindow
from FE.AddAccount.addAccount import AddAccount


class Main_Window(Ui_MainWindow):
    def __init__(self):
        # Setup Main window UI
        self.dialog = AddAccount()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)

        # Add border to table header
        self.tableAccInfo.setStyleSheet("QHeaderView::section { border: 1px solid black}")

        # Connect signals
        self.buttonAddAccount.clicked.connect(self.openDialog)

    # Connect signals method
    def openDialog(self, modal=True):
        self.dialog.show()

    # Other method
    def showTable(self, data):
        # for i in range(0, len(ds)):
        #     self.tableAccInfo.setItem(row=i, column=1, item=str(data[0]))
        #     self.tableAccInfo.setItem(row=i, column=1, item=str(data[1]))
        #     self.tableAccInfo.setItem(row=i, column=1, item=str(data[2]))
        return

    # Show UI
    def show(self):
        self.MainWindow.show()
