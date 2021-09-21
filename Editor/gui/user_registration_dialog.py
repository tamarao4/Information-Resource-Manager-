from PySide2 import QtWidgets, QtGui
from handler.login.login_handler import LoginHandler


class UserRegistrationDialog(QtWidgets.QDialog):
    def __init__(self, userFile):
        super(UserRegistrationDialog, self).__init__()
        self.setWindowTitle('Registracija')
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.handler = LoginHandler(userFile)
        self.btn_ok = QtWidgets.QPushButton('OK')
        self.btn_cancel = QtWidgets.QPushButton('Cancel')
        self.btn_ok.clicked.connect(self.register)
        self.btn_cancel.clicked.connect(self.reject)

        self.txt_user = QtWidgets.QLineEdit()
        self.txt_pass = QtWidgets.QLineEdit()
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        layout = QtWidgets.QFormLayout()
        layout.addRow(QtWidgets.QLabel('Korisnico ime'), self.txt_user)
        layout.addRow(QtWidgets.QLabel('Lozinka'), self.txt_pass)
        box = QtWidgets.QDialogButtonBox()
        box.addButton(self.btn_ok, QtWidgets.QDialogButtonBox.AcceptRole)
        box.addButton(self.btn_cancel, QtWidgets.QDialogButtonBox.RejectRole)
        layout.addRow(box)
        self.setLayout(layout)
        self.user = None
        return

    def register(self):
        username = self.txt_user.text()
        password = self.txt_pass.text()
        created = self.handler.createUser(username, password)
        if created:
            self.accept()
        else:
            QtWidgets.QMessageBox.information(self, 'Nije moguce kreirati korisnika', 'Kosisnicko ime je zauzeto ili je neispravan unos.')

    def get_data(self):
        return self.user
