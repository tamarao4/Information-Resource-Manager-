from PySide2 import QtWidgets, QtGui
from handler.serial_file_handler import SerialFileHandler
from model.visokoskolska_ustavnova import VisokoskolskaUstanova


class AddRowDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AddRowDialog, self).__init__()
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.setWindowTitle("Dodavanje nove visokoskolske ustanove")
        self.resize(500, 100)
        set_layout = QtWidgets.QFormLayout()

        self.input_1 = QtWidgets.QLineEdit()
        self.input_2 = QtWidgets.QLineEdit()
        self.input_3 = QtWidgets.QLineEdit()

        set_layout.addRow(QtWidgets.QLabel("Oznaka: "), self.input_1)
        set_layout.addRow(QtWidgets.QLabel("Naziv: "), self.input_2)
        set_layout.addRow(QtWidgets.QLabel("Adresa: "), self.input_3)

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
        if self.input_1.text() == "" or self.input_2.text() == "" or self.input_3 == "":
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Upozorenje!")
            msg_box.setWindowIcon(QtGui.QIcon('res/icons/wrr.png'))
            msg_box.setText("Morate popuniti sva polja.")
            msg_box.exec()
        else:
            serial_file_handler = SerialFileHandler("data/visokoskolska_ustanova_data", "data/visokoskolska_ustanova_metadata.json")
            vs = (VisokoskolskaUstanova(self.input_1.text(), self.input_2.text(), self.input_3.text(), [], []))
            serial_file_handler.insert(vs)
        # salje true nakon exec_()
        self.accept()
