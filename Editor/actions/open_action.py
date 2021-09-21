from PySide2 import QtWidgets, QtGui
from gui.open_project_dalog import OpenProjectDialog


class OpenAction(QtWidgets.QAction):
    def __init__(self):
        super(OpenAction, self).__init__('Otvori', None)
        self.setIcon(QtGui.QIcon('res/icons/open.png'))
        self.triggered.connect(self.execute)
        self.putanja = ""

    def execute(self):
        dialog = OpenProjectDialog()
        dialog.exec_()
        self.putanja = dialog.getResult()

    def getResult(self):
        return self.putanja
