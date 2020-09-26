from PyQt5 import QtCore

from .window import Window


class WindowSignal(Window, QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    # signal_object = QtCore.pyqtSignal(str, object)

    def __init__(self):
        super().__init__()
