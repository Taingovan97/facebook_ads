from .MainWindow.mainWindow import Main_Window
from .AddAccount.addAccount import AddAccount
from .AddVia.addVia import AddVia
from .utils_FE import show_popup


class UIController:
    def __init__(self):
        self.main_window = Main_Window()
        self.dialog = None

    def show_main_window(self):
        # self.main_window.signal.connect(self.signal_process)
        # self.main_window.signal_object.connect(self.signal_object_process)
        self.main_window.buttonAddAccount.clicked.connect(lambda: self.signal_process("OpenAddAccountDialog"))
        self.main_window.actionAddVia.triggered.connect(lambda: self.signal_object_process(
            "OpenAddViaDialog", self.main_window.selectedList))
        self.main_window.show()

    def signal_process(self, msg: str):
        if "OpenAddAccountDialog" == msg:
            self.dialog = AddAccount()
            self.dialog.signal.connect(self.process_signals_from_AddAccount)
            self.dialog.show()

        if "OpenAddViaDialog" == msg:
            self.dialog = AddVia()
            self.dialog.signal.connect(self.process_signals_from_AddVia)
            self.dialog.show()

    def signal_object_process(self, msg: str, obj: object):
        if "OpenAddViaDialog" == msg:
            if obj:
                self.dialog = AddVia(seleted_uid_list=obj)
                self.dialog.signal.connect(self.process_signals_from_AddVia)
                self.dialog.show()
            else:
                show_popup(title="Chưa chọn", msg="Chưa chọn tài khoản nào, vui lòng chọn ít nhất 1 "
                                                  "tài khoản")

    def process_signals_from_AddAccount(self, msg):
        if "ShowTable" == msg:
            self.main_window.showTable()

    def process_signals_from_AddVia(self, msg):
        if "ShowTable" == msg:
            self.main_window.showTable()
