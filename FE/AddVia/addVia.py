# Process in addVia UI
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from FE.AddVia.addVia_UI_PY import Ui_AddVia
from FE.windowSignal import WindowSignal


class AddVia(Ui_AddVia, WindowSignal):
    def __init__(self,
                 seleted_uid_list=None,
                 modal=True):
        super().__init__()
        if seleted_uid_list is None:
            seleted_uid_list = []
        self.selete_uid_list = seleted_uid_list
        self.modal = modal

        # Add setup Add Via UI
        self.Dialog = QDialog()
        self.Dialog.setModal(self.modal)
        self.setupUi(self.Dialog)
        self.Dialog.setFixedSize(800, 500)

        # Setup table
        self.tableSeletedAccount.setColumnWidth(0, 120)
        # Add border to table header
        self.tableSeletedAccount.setStyleSheet("QHeaderView::section { border: 1px solid black}")

        # Show table
        self.showTable()

        # Connect signals
        self.buttonStart.clicked.connect(self.start)

    # Connect signals method
    def start(self):
        text = self.lineEditAccVia.text()
        acc = text.split("|")
        for ele in acc.copy():
            if ele == "":
                acc.remove(ele)
        if len(acc) == 3:
            # Acc will be [uid, pass, code2fa]

            WindowSignal._service.add_via()

    # Other method
    def showTable(self):
        self.tableSeletedAccount.setRowCount(0)
        for row_number, account in enumerate(WindowSignal._service.get_seleted_table(self.selete_uid_list)):
            self.tableSeletedAccount.insertRow(row_number)
            acc = [account.uid, account.status]
            for column_num, column_data in enumerate(acc):
                self.tableSeletedAccount.setItem(row_number, column_num, QTableWidgetItem(column_data))

    # Show UI
    def show(self):
        self.Dialog.show()
