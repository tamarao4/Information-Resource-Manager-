from PySide2 import QtWidgets, QtGui, QtCore
from gui.glavna_tabela import GlavnaTabela


class WorkspaceView(QtWidgets.QMainWindow):
    def __init__(self, workspace):
        super(WorkspaceView, self).__init__()
        self.workaspace = workspace
        
        self.init_toolbar_ws()
        self.prikazana_tabela = False
        self.pritisnuto_dugme = 0

        self.lista_putanja = []
        self.kreiraj_lisut_putanja()

        # self.lista_putanja.append("C:/Users/Tamara/Desktop/baze-podataka/Editor/data/visokoskolska_ustanova_data")
        # self.lista_putanja.append("C:/Users/Tamara/Desktop/baze-podataka/Editor/data/nivo_studija_data")
        # self.lista_putanja.append("C:/Users/Tamara/Desktop/baze-podataka/Editor/data/nastavni_predmet_data")
        # self.lista_putanja.append("C:/Users/Tamara/Desktop/baze-podataka/Editor/data/tok_studija_data")

    def kreiraj_lisut_putanja(self):
        try:
            f = open("putanja.txt", "r")
            self.otvoren_fajl = f.read()
            self.lista_putanja.append(self.otvoren_fajl)
        except Exception:
            pass

    def init_toolbar_ws(self):
        self.toolbar = QtWidgets.QToolBar("Alati za rad sa tabelama")
    # osvezi kad ucitas da se prikaze
        osvezi = QtWidgets.QAction(self.toolbar)
        osvezi.setText('Ponovo ucitaj')
        osvezi.setIcon(QtGui.QIcon('res/icons/refresh.png'))
        osvezi.triggered.connect(self.create_tab)
        self.toolbar.addAction(osvezi)
    # kreiraj tabelu
        create_table = QtWidgets.QAction(self.toolbar)
        create_table.setText('Kreiraj praznu tabelu')
        create_table.setIcon(QtGui.QIcon('res/icons/add.png'))
        create_table.triggered.connect(self.new_table)
        self.toolbar.addAction(create_table)
    # kreiraj podtabelu
        create_subtable = QtWidgets.QAction(self.toolbar)
        create_subtable.setText('Kreiraj povezanu tabelu')
        create_subtable.setIcon(QtGui.QIcon('res/icons/subtable.png'))
        create_subtable.triggered.connect(self.create_subtab)
        self.toolbar.addAction(create_subtable)
    # dodavanje reda u tabelu
        add_row = QtWidgets.QAction(self.toolbar)
        add_row.setText("Dodaj red")
        add_row.setIcon(QtGui.QIcon('res/icons/new_row.png'))
        add_row.triggered.connect(self.add_row_action)
        self.toolbar.addAction(add_row)
    # brisanje reda
        del_row = QtWidgets.QAction(self.toolbar)
        del_row.setText("Obrisi red")
        del_row.setIcon(QtGui.QIcon('res/icons/delete_row.png'))
        del_row.triggered.connect(self.del_row_action)
        self.toolbar.addAction(del_row)
        # dodavnje toolbara da bude viljiv
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolbar)

    def add_row_action(self):
        if self.prikazana_tabela is True:
            # postoji i dijalog koji sam koristila,
            # ali se on moze kkoristi samo za dodavanje viskoskolskih ustanova
            self.pritisnuto_dugme = 1
            self.create_tab()
            self.pritisnuto_dugme = 0
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Upozorenje!")
            msg_box.setWindowIcon(QtGui.QIcon('res/icons/wrr.png'))
            msg_box.setText('Ne možete dodati red, ako nije prikazana tabela.  ')
            msg_box.exec()

    def del_row_action(self, index):
        if self.prikazana_tabela is True:
            # dialog = DeleteRowDialog()
            # dialog.exec_()
            # automatski se refresuje
            self.pritisnuto_dugme = 2
            self.create_tab()
            self.pritisnuto_dugme = 0
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Upozorenje!")
            msg_box.setWindowIcon(QtGui.QIcon('res/icons/wrr.png'))
            msg_box.setText('Ne možete ukloniti red, ako nije prikazana tabela.  ')
            msg_box.exec()
            
    def create_tab(self):
        self.lista_putanja = []
        self.kreiraj_lisut_putanja()
        tab = QtWidgets.QTabWidget(self)
        # print("Lista putanja u fji za kriranje lista", self.lista_putanja)
        for putanja in self.lista_putanja:
            glavna_tabela = GlavnaTabela(putanja, self.pritisnuto_dugme)
            naslov = self.naslov_taba(putanja)
            tab.addTab(glavna_tabela, QtGui.QIcon("res/icons8-edit-file-64.png"), naslov)
            tab.setTabsClosable(True)
            # TODO: treba postaviti da moze da se zatvori tab
            tab.setMovable(True)
            self.setCentralWidget(tab)
            self.prikazana_tabela = True
        self.pritisnuto_dugme = 0

    def new_table(self):
        self.lista_putanja = [""]
        tab = QtWidgets.QTabWidget(self)
        # print("Lista putanja u fji za kriranje lista", self.lista_putanja)
        for putanja in self.lista_putanja:
            glavna_tabela = GlavnaTabela(putanja, self.pritisnuto_dugme)
            naslov = self.naslov_taba(putanja)
            tab.addTab(glavna_tabela, QtGui.QIcon("res/icons8-edit-file-64.png"), naslov)
            tab.setTabsClosable(True)
            # TODO: treba postaviti da moze da se zatvori tab
            tab.setMovable(True)
            self.setCentralWidget(tab)
            self.prikazana_tabela = True
        self.pritisnuto_dugme = 0

    def remove_tab(self, index):
        self.removeTab(index)

    def create_subtab(self):
        if self.prikazana_tabela is False:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Upozorenje!")
            msg_box.setWindowIcon(QtGui.QIcon('res/icons/wrr.png'))
            msg_box.setText(' Nije moguće dodati povezanu tabelu pre glavne.  ')
            msg_box.exec()
        print("ne znam da li ce biti moguce, ni kako sam ovo zimislila")

    def naslov_taba(self, putanja):
        naslov = putanja.split("/")
        naslov = str(naslov[-1])
        naslov = naslov.replace("_data", "")
        naslov = naslov.replace("_", " ")
        return naslov
