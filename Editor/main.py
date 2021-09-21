import sys
from PySide2 import QtWidgets
from gui.login_dialog import LoginDialog
from gui.main_window import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pixmap = QtWidgets.QGraphicsPixmapItem('res/icons8-edit-file-64.png')
    # app.selection = None
    login_dlg = LoginDialog('korisnici.cfg')
    login_dlg.show()
    if login_dlg.exec_():
        user_profile = login_dlg.get_data()
        app.profile = user_profile
        app.main_window = MainWindow()
        app.main_window.show()
    # else:
        # moze da se porkene glavni prozori i ako je korisnik gost
        # TODO: ovo nece biti u konacnoj verziji ali je sada lakse za test
        # app.main_window = MainWindow()
        # app.main_window.show()

    sys.exit(app.exec_())
