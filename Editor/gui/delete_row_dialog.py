from PySide2 import QtWidgets, QtGui
from handler.serial_file_handler import SerialFileHandler
from model.visokoskolska_ustanova_model import VisokoskolskaUstanovaModel


class DeleteRowDialog(QtWidgets.QDialog):
    def __init__(self):
        super(DeleteRowDialog, self).__init__()
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.setWindowTitle("Uklanjanje reda iz tabelu")
        self.resize(500, 100)
        set_layout = QtWidgets.QFormLayout()

        self.input_1 = QtWidgets.QLineEdit()

        set_layout.addRow(QtWidgets.QLabel("Broj indeksa: "), self.input_1)

        btn_ok = QtWidgets.QPushButton("OK")
        btn_ok.clicked.connect(self.ok_action)
        btn_cancel = QtWidgets.QPushButton("Cancel")
        # salje false nakon exec_()
        btn_cancel.clicked.connect(self.reject)

        group = QtWidgets.QDialogButtonBox()
        group.addButton(btn_ok, QtWidgets.QDialogButtonBox.AcceptRole)
        group.addButton(btn_cancel, QtWidgets.QDialogButtonBox.RejectRole)

        set_layout.addRow(group)
        self.setLayout(set_layout)

    def ok_action(self):
        if self.input_1.text() == "":
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Upozorenje!")
            msg_box.setWindowIcon(QtGui.QIcon('res/icons/wrr.png'))
            msg_box.setText("Morate popuniti sva polja.")
            msg_box.exec()
        else:
            serial_file_handler = SerialFileHandler("data/visokoskolska_ustanova_data", "data/visokoskolska_ustanova_metadata.json")
            serial_file_handler.delete_one(id)

        # salje true nakon exec_()
        self.accept()
