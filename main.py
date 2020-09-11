import sys
from PyQt5.QtWidgets import QApplication
from FE.MainWindow import MainWindow
from BE import api, constants

if __name__ == "__main__":

    driver_clone = api.login(constants.username_clone, constants.pass_clone, constants.key2fa_clone, idUser='12345678')

    #driver_via = api.login(constants.username_via, constants.pass_via, constants.key2fa_via, idVia, idClone)

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

