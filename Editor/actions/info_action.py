from PySide2 import QtWidgets, QtGui


class InfoAction(QtWidgets.QAction):
    def __init__(self):
        super(InfoAction, self).__init__('Info', None)
        self.setIcon(QtGui.QIcon('res/icons/info.png'))
        self.triggered.connect(self.execute)

    def execute(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Informacije o bagovima!")
        msg_box.setWindowIcon(QtGui.QIcon('res/icons/info.png'))
        poruka = self.ucitaj_poruku()
        msg_box.setText(poruka)
        msg_box.exec()

    def ucitaj_poruku(self):
        f = open("bagovi.txt", "r")
        return f.read()
