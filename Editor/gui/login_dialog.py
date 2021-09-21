from PySide2 import QtWidgets, QtGui
from gui.user_registration_dialog import UserRegistrationDialog
from handler.login.login_handler import LoginHandler


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, userFile):
        super(LoginDialog, self).__init__()
        self.setWindowTitle('Prijava')
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.userFile = userFile
        self.handler = LoginHandler(userFile)
        self.btnOk = QtWidgets.QPushButton('OK')
        self.btnCancel = QtWidgets.QPushButton('Cancel')

        self.btnOk.clicked.connect(self.login)
        self.btnCancel.clicked.connect(self.reject)

        self.txt_user = QtWidgets.QLineEdit()
        self.txt_pass = QtWidgets.QLineEdit()
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        layout = QtWidgets.QFormLayout()
        layout.addRow(QtWidgets.QLabel('Korisnicko ime'), self.txt_user)
        layout.addRow(QtWidgets.QLabel('Lozinka'), self.txt_pass)
        box = QtWidgets.QDialogButtonBox()
        box.addButton(self.btnOk, QtWidgets.QDialogButtonBox.AcceptRole)
        box.addButton(self.btnCancel, QtWidgets.QDialogButtonBox.RejectRole)
        layout.addRow(box)
        btn_register = QtWidgets.QPushButton('Registruj se')
        btn_register.clicked.connect(self.register_user)
        layout.addRow(btn_register)
        self.setLayout(layout)
        self.user = None
        return

    def login(self):
        username = self.txt_user.text()
        password = self.txt_pass.text()
        user = self.handler.login_user(username, password)
        if user is not None:
            self.user = user
            self.accept()
        else:
            QtWidgets.QMessageBox.information(self, 'Neuspesna prijava', 'Nije uspela pijrava, pokusajete ponovo')
        return

    def get_data(self):
        return self.user

    def register_user(self):
        usr_reg_dlg = UserRegistrationDialog(self.userFile)
        usr_reg_dlg.exec_()
