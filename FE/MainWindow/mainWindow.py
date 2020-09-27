# Process in mainwindow UI


from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt5.QtCore import Qt

from FE.MainWindow.mainWindow_UI_PY import Ui_MainWindow
from FE.AddAccount.addAccount import AddAccount
from FE.utils_FE import show_popup
from FE.window import Window


class Main_Window(Ui_MainWindow, Window):
    def __init__(self):
        super().__init__()
        # Save list in form [uid, ...]
        self.selectedList = []

        # Add setup Main window UI
        self.dialog = AddAccount()
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.setFixedSize(1200, 700)

        # Setup table
        self.tableAccInfo.setColumnWidth(0, 25)
        self.tableAccInfo.setColumnWidth(1, 120)
        self.tableAccInfo.setColumnWidth(2, 120)
        self.tableAccInfo.setColumnWidth(3, 120)
        self.tableAccInfo.setColumnWidth(4, 230)
        self.tableAccInfo.setColumnWidth(5, 120)
        self.tableAccInfo.setColumnWidth(6, 120)
        self.tableAccInfo.setColumnWidth(7, 120)
        self.tableAccInfo.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # Add border to table header
        self.tableAccInfo.setStyleSheet("QHeaderView::section { border: 1px solid black}")

        # Show table
        self.showTable()

        # Connect signals
        self.buttonDeleteAccount.clicked.connect(self.deleteSelectedAccount)
        self.buttonCreateScript.clicked.connect(self.createScript)
        self.checkBoxAll.stateChanged.connect(self.checkAll)
        self.tableAccInfo.itemClicked.connect(self.handleItemClicked)
        self.buttonLogin.clicked.connect(self.login)
        # self.buttonLogin(self.login)

    # Connect signals method
    def login(self):
        Window._service.login(listUid=self.selectedList)

    def createScript(self):
        print("Script")
        print("clicked!")

    def handleItemClicked(self, item):
        # if item.column() == 0:
        checkbox = self.tableAccInfo.item(item.row(), 0)
        selectedItemText = self.tableAccInfo.item(item.row(), 1).text()
        if checkbox.checkState() == Qt.Unchecked:
            checkbox.setCheckState(Qt.Checked)
            for column in range(self.tableAccInfo.columnCount()):
                self.tableAccInfo.item(item.row(), column).setBackground(Qt.lightGray)
            if selectedItemText not in self.selectedList:
                self.selectedList.append(selectedItemText)

        elif checkbox.checkState() == Qt.Checked:
            checkbox.setCheckState(Qt.Unchecked)
            for column in range(self.tableAccInfo.columnCount()):
                self.tableAccInfo.item(item.row(), column).setBackground(Qt.white)
            if selectedItemText in self.selectedList:
                self.selectedList.remove(selectedItemText)

    def checkAll(self, state):
        if state == Qt.Checked:
            for row in range(0, self.tableAccInfo.rowCount()):
                checkbox = self.tableAccInfo.item(row, 0)
                checkbox.setCheckState(Qt.Unchecked)
                self.handleItemClicked(checkbox)
        elif state == Qt.Unchecked:
            for row in range(0, self.tableAccInfo.rowCount()):
                checkbox = self.tableAccInfo.item(row, 0)
                checkbox.setCheckState(Qt.Checked)
                self.handleItemClicked(checkbox)
        self.tableAccInfo.clearSelection()

    def deleteSelectedAccount(self):
        if len(self.selectedList) > 0:
            Window._service.delete_list_account(self.selectedList)
            self.showTable()
        else:
            show_popup(title="Chưa chọn", msg="Chưa chọn tài khoản nào, vui lòng chọn ít nhất 1 "
                                              "tài khoản")

    # Other method
    def showTable(self):
        self.selectedList = []
        self.checkBoxAll.setCheckState(Qt.Unchecked)
        self.tableAccInfo.setRowCount(0)
        for row_number, account in enumerate(Window._service.get_full_table()):
            self.tableAccInfo.insertRow(row_number)
            acc = [account.uid, account.name, account.password, account.code2fa, account.cookie,
                   account.token, account.bank, account.status]
            for column_num, column_data in enumerate(acc):
                checkbox = QTableWidgetItem()
                checkbox.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                checkbox.setCheckState(Qt.Unchecked)
                self.tableAccInfo.setItem(row_number, 0, checkbox)
                self.tableAccInfo.setItem(row_number, column_num + 1, QTableWidgetItem(column_data))

    # def get_uid_selected_list_from_row(self):
    #     listuid = []
    #     for row in self.selectedList:
    #         listuid.append(self.tableAccInfo.item(row, 1).text())
    #     return listuid

    # Show UI
    def show(self):
        self.MainWindow.show()
