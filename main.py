import sys
from PyQt5.QtWidgets import QApplication
from FE.MainWindow.mainWindow import Main_Window
# from BE.core import constants, api

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Main_Window()
    main_win.show()
    sys.exit(app.exec_())
