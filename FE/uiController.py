from .MainWindow.mainWindow import Main_Window
from .AddAccount.addAccount import AddAccount

class UIController:
    def __init__(self):
        self.main_window = Main_Window()
        self.dialog = None

    def show_main_window(self):
        self.main_window.signal.connect(self.show_dialog)
        self.main_window.show()

    def show_dialog(self, msg):
        if "AddAccount" == msg:
            self.dialog = AddAccount()
            self.dialog.signal.connect(self.process_signals_from_AddAccount)
            self.dialog.show()

    def process_signals_from_AddAccount(self, msg):
        if "ShowTable" == msg:
            self.main_window.showTable()
