from PySide2 import QtWidgets, QtGui
# treba napraviti dijalog za uklanjanje projekta, za potvrdu
from gui.remove_project_dialog import RemoveProjectDialog


class RemoveAction(QtWidgets.QAction):
    def __init__(self):
        super(RemoveAction, self).__init__('Obriši', None)
        self.setIcon(QtGui.QIcon('res/icons/delete.png'))
        self.triggered.connect(self.execute)

    def execute(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("Data Files (*data)")
        if dialog.exec_():  # mora, da bi se dijalog prikazao
            file_name = dialog.selectedFiles()
        selected_file = file_name[0]
        dijalog = RemoveProjectDialog(selected_file)
        dijalog.exec_()
