from PySide2 import QtWidgets, QtGui


class OpenProjectDialog(QtWidgets.QDialog):
    def __init__(self):
        super(OpenProjectDialog, self).__init__()
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.setWindowTitle("Otvaranje fajla")
        self.resize(500, 100)
        self.set_layout = (QtWidgets.QVBoxLayout())
        layout_1 = QtWidgets.QHBoxLayout()
        layout_2 = QtWidgets.QHBoxLayout()  # da napravim razmak
        self.file_path = QtWidgets.QLineEdit()
        self.file_path.setReadOnly(True)
        self.file_path.setMinimumWidth(50)
        action_browse = QtWidgets.QPushButton(' ... ')
        action_browse.setMinimumWidth(50)
        action_browse.clicked.connect(self.browse)
        layout_1.addWidget(self.file_path)
        layout_1.addWidget(action_browse)
        self.btn_ok = QtWidgets.QPushButton('OK')
        self.btn_ok.clicked.connect(self.ok)
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
        self.result = ""

    def browse(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        # mogu otvoriti samo fajlove koji sadrze data u nazivu i nemaju ekst
        dialog.setNameFilter("Data Files (*data)")
        if dialog.exec_():  # mora, da bi se dijalog prikazao
            file_name = dialog.selectedFiles()

        self.file_path.setText(file_name[0])
        self.result = file_name[0]

    def ok(self):
        self.accept()

    def cancel(self):
        self.reject()

    def getResult(self):
        return self.result
