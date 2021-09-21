from PySide2 import QtWidgets, QtGui
from handler.file_handler import FileHandler


class CreateProjectDialog(QtWidgets.QDialog):
    def __init__(self):
        super(CreateProjectDialog, self).__init__()
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.setWindowTitle("Odabir putanje za kreiranje fajla")
        self.resize(500, 100)
        self.set_layout = (QtWidgets.QVBoxLayout())
        layout_1 = QtWidgets.QHBoxLayout()
        layout_2 = QtWidgets.QHBoxLayout()  # da napravim razmak
        self.path = QtWidgets.QLineEdit()
        self.path.setReadOnly(True)
        self.path.setMinimumWidth(50)
        action_browse = QtWidgets.QPushButton(' ... ')
        action_browse.setMinimumWidth(50)
        action_browse.clicked.connect(self.browse)
        layout_1.addWidget(self.path)
        layout_1.addWidget(action_browse)
        self.btn_cancel = QtWidgets.QPushButton('Cancel')
        self.btn_cancel.clicked.connect(self.cancel)
        box = QtWidgets.QDialogButtonBox()
        box.addButton(self.btn_cancel, QtWidgets.QDialogButtonBox.RejectRole)
        layout = QtWidgets.QFormLayout()
        layout.addRow(layout_1)
        layout.addRow(layout_2)

        layout.addWidget(box)
        self.setLayout(layout)
        # treba mi signal
        self.result = ""

    def browse(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        if dialog.exec_():  # mora, da bi se dijalog prikazao
            file_names = dialog.selectedFiles()
        # try:
        select_file = file_names[0]
        self.path.setText(select_file)  # ovo mi daje memorijsku lokaciju
        fh = FileHandler()
        name, ok = QtWidgets.QInputDialog.getText(self, 'Novi Fajl', 'Unesite ime fajal:')
        if ok:
            if name == "":
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Upozorenje!")
                msg_box.setWindowIcon(QtGui.QIcon('res/icons/wrr.png'))
                msg_box.setText('Morate da unesete naziv fajla.  ')
                msg_box.exec()
            else:
                fh.create_file(select_file, name)
                print("proslo je kreiranje fajla")
                self.reject()
            self.reject()

    def cancel(self):
        self.reject()
