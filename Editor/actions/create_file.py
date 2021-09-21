from PySide2 import QtWidgets, QtGui
from gui.create_project_dialog import CreateProjectDialog


class CreateFile(QtWidgets.QAction):
    def __init__(self):
        super(CreateFile, self).__init__('Kreiraj Fajl', None)
        self.setIcon(QtGui.QIcon('res/icons/file.png'))
        self.triggered.connect(self.execute)

    def execute(self, index):
        dialog = CreateProjectDialog()
        dialog.exec_()
