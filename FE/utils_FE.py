from PyQt5.QtWidgets import QMessageBox


def show_popup(title: str, msg: str):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setText(msg)
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec_()