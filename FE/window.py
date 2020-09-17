from PyQt5 import QtCore

from BE.service import Service


class Window(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._service = Service()
