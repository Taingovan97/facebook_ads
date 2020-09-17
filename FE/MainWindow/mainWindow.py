# Process in mainwindow UI


from PyQt5 import QtWidgets, QtCore

from FE.MainWindow.mainWindow_UI_PY import Ui_MainWindow
from FE.AddAccount.addAccount import AddAccount
from FE.window import Window


class Main_Window(Ui_MainWindow, Window):
    def __init__(self):
        super().__init__()
        self.selectedList = []

        # Add setup Main window UI
        self.dialog = AddAccount()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.setFixedSize(1200, 700)

        # Setup table
        self.tableAccInfo.setColumnWidth(0, 25)
        self.tableAccInfo.setColumnWidth(1, 120)
        self.tableAccInfo.setColumnWidth(2, 120)
        self.tableAccInfo.setColumnWidth(3, 120)
        self.tableAccInfo.setColumnWidth(4, 200)

        # Add border to table header
        self.tableAccInfo.setStyleSheet("QHeaderView::section { border: 1px solid black}")

        # Show table
        self.showTable()

        # Connect signals
        self.buttonAddAccount.clicked.connect(lambda: self.openDialog("AddAccount"))
        self.buttonDeleteAccount.clicked.connect(self.deleteSelectedAccount)
        self.buttonCreateScript.clicked.connect(self.createScript)
        self.checkBoxAll.stateChanged.connect(self.checkAll)
        self.tableAccInfo.itemClicked.connect(self.handleItemClicked)

    # Connect signals method
    def openDialog(self, msg: str):
        self.signal.emit(msg)

    def createScript(self):
        print("Script")
        print("clicked!")

    def handleItemClicked(self, item):
        if item.column() == 0:
            if item.checkState() == QtCore.Qt.Checked:
                if item.row() not in self.selectedList:
                    self.selectedList.append(item.row())
            elif item.checkState() == QtCore.Qt.Unchecked:
                if item.row() in self.selectedList:
                    self.selectedList.remove(item.row())

    def checkAll(self, state):
        if state == QtCore.Qt.Checked:
            for row in range(0, self.tableAccInfo.rowCount()):
                checkbox = self.tableAccInfo.item(row, 0)
                checkbox.setCheckState(QtCore.Qt.Checked)
                self.handleItemClicked(checkbox)
        elif state == QtCore.Qt.Unchecked:
            for row in range(0, self.tableAccInfo.rowCount()):
                checkbox = self.tableAccInfo.item(row, 0)
                checkbox.setCheckState(QtCore.Qt.Unchecked)
                self.handleItemClicked(checkbox)

    def deleteSelectedAccount(self):
        # self.selectedList.sort(reverse=True)
        listuid = []
        for row in self.selectedList:
            # self._service.delete_account(self.tableAccInfo.item(row, 1).text())
            listuid.append(self.tableAccInfo.item(row, 1).text())
        if len(listuid) > 0:
            self._service.delete_list_account(listuid)
            self.showTable()

    # Other method
    def showTable(self):
        self.selectedList = []
        self.checkBoxAll.setCheckState(QtCore.Qt.Unchecked)
        self.tableAccInfo.setRowCount(0)
        for row_number, account in enumerate(self._service.get_table()):
            self.tableAccInfo.insertRow(row_number)
            acc = [account.uid, account.name, account.password, account.code2fa, account.cookie,
                   account.token, account.bank, account.status]
            for column_num, column_data in enumerate(acc):
                checkbox = QtWidgets.QTableWidgetItem()
                checkbox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                checkbox.setCheckState(QtCore.Qt.Unchecked)
                self.tableAccInfo.setItem(row_number, 0, checkbox)
                self.tableAccInfo.setItem(row_number, column_num + 1, QtWidgets.QTableWidgetItem(column_data))

    # Show UI
    def show(self):
        self.MainWindow.show()
