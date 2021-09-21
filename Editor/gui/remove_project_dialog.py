from PySide2 import QtGui, QtWidgets, QtCore
from handler.file_handler import FileHandler


class RemoveProjectDialog(QtWidgets.QDialog):
    def __init__(self, file_name):
        super(RemoveProjectDialog, self).__init__()
        self.file_name = file_name
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.set_layout = (QtWidgets.QVBoxLayout())
        layout_1 = QtWidgets.QHBoxLayout()
        layout_1.addWidget(QtWidgets.QLabel('Da li ste sigruni da želite da obrišete?'))
        layout_2 = QtWidgets.QHBoxLayout()
        self.remove_from_disk = QtWidgets.QCheckBox('Ukloni sa diska.')
        layout_2.addWidget(self.remove_from_disk)
        layout_2.addStretch()
        self.btn_ok = QtWidgets.QPushButton('OK')
        self.btn_ok.clicked.connect(self.remove)
        self.btn_cancel = QtWidgets.QPushButton('Cancel')
        self.btn_cancel.clicked.connect(self.cancel)
        box = QtWidgets.QDialogButtonBox()
        box.addButton(self.btn_ok, QtWidgets.QDialogButtonBox.AcceptRole)
        box.addButton(self.btn_cancel, QtWidgets.QDialogButtonBox.RejectRole)
        layout = QtWidgets.QFormLayout()
        layout.addRow(layout_1)
        layout.addRow(layout_2)
        layout.addWidget(box)
        self.setLayout(layout)

    def cancel(self):
        self.reject()

    def remove(self):
        print(self.file_name)
        split_path = self.file_name.split("/")
        name = split_path[-1]
        print(name)
        if self.remove_from_disk.isChecked():
            fh = FileHandler()
            fh.removeFile(self.file_name)
            self.reject()
        else:
            # TODO: izbrisati ga samo sa prikaza u projetu
            self.accept()
