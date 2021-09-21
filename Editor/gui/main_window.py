from PySide2 import QtCore, QtWidgets, QtGui
from gui.workspace_view import WorkspaceView
from handler.serial_file_handler import SerialFileHandler

# akcije odvojene za toolbar
from actions.action_manager import ActionManager
# potrebno za statusbar
from time import gmtime, strftime


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        screen_size = QtWidgets.QDesktopWidget.screenGeometry(QtWidgets.QApplication.desktop())
        w = screen_size.width()
        h = screen_size.height()
        self.setGeometry(w / 4, h / 4, w / 2, h / 2)
        self.setWindowIcon(QtGui.QIcon('res/icons8-edit-file-64.png'))
        self.tree = self.init_tree()
        # akcije za toolbar
        self.action_manager = ActionManager()
        self.setWindowTitle('Rukovalac informacionim resursima')
        self.workspace = self.init_central()
        self.init_toolbar()
        self.init_menu()
        self.init_statusbar()
        self.action_manager.open_action.triggered.connect(self.dobavi_putanju)
        self.putanja_fajla = ""

    def dobavi_putanju(self):
        # mozda bi ovo moglo i preko signala, ali nisam uspela
        self.putanja_fajla = self.action_manager.open_action.getResult()
        # ws = WorkspaceView(self)
        # ws.kriraj_lisut_putanja(self.putanja_fajla)
        f = open("putanja.txt", "w")
        f.write(self.putanja_fajla)
        f.close()

    def init_tree(self):
        self.structure_dock = QtWidgets.QDockWidget("Prikaz sturkture informacionog sistema", self)
        # da uzme putanju fajl
        file_system_model = QtWidgets.QFileSystemModel()
        file_system_model.setRootPath(QtCore.QDir.currentPath())
        tree_view = QtWidgets.QTreeView()
        tree_view.setModel(file_system_model)
        # da krene od trenutne lokacije
        tree_view.setRootIndex(file_system_model.index(QtCore.QDir.currentPath()))
        self.structure_dock.setWidget(tree_view)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.structure_dock)

    def init_central(self):
        self.setCentralWidget(WorkspaceView(QtWidgets.QApplication.instance()))

    def init_toolbar(self):
        self.toolbar = QtWidgets.QToolBar("Alati za rad sa fajlovima")
        # dodajem akcije za otvaranje u toolbar TODO: poziv akcije
        self.toolbar.addAction(self.action_manager.open_action)
        # sacuvaj
        save = QtWidgets.QAction(self.toolbar)
        save.setText('Sačuvaj')
        save.setIcon(QtGui.QIcon('res/icons/save.png'))
        save.triggered.connect(self.save_doc)
        self.toolbar.addAction(save)
        # dodaj tabelu
        self.toolbar.addAction(self.action_manager.create_file)
        # dodajem akcije za uklanjanje u toolbar TODO: poziv akcije
        self.toolbar.addAction(self.action_manager.remove_action)
        self.toolbar.toggleViewAction()
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolbar)

    def init_menu(self):
        file_menu = QtWidgets.QMenu("File")
        edit_menu = QtWidgets.QMenu("Edit")
        view_menu = QtWidgets.QMenu("View")
        help_menu = QtWidgets.QMenu("Help")

        file_menu.addAction(self.action_manager.open_action)
        edit_menu.addAction(self.action_manager.remove_action)
        file_menu.addAction(self.action_manager.create_file)
        toggle_structure_dock_action = self.structure_dock.toggleViewAction()
        view_menu.addAction(toggle_structure_dock_action)
        toggle_toolbar = self.toolbar.toggleViewAction()
        view_menu.addAction(toggle_toolbar)
        help_menu.addAction(self.action_manager.inof_action)

        self.menuBar().addMenu(file_menu)
        self.menuBar().addMenu(edit_menu)
        self.menuBar().addMenu(view_menu)
        self.menuBar().addMenu(help_menu)

    def save_doc(self):
        if self.putanja_fajla != "":
            metadata = self.meta_filepaht()
            sfh = SerialFileHandler(self.putanja_fajla, metadata)
            sfh.save_to_file()
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Save")
            msg_box.setWindowIcon(QtGui.QIcon('res/icons/save.png'))
            poruka = str(' Izmene su sačuvane, u fajlu: \n' + self.putanja_fajla)
            msg_box.setText(poruka)
            msg_box.exec()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Save")
            msg_box.setWindowIcon(QtGui.QIcon('res/icons/save.png'))
            msg_box.setText(' Nepoznat fajl koji treba sacuvati. ')
            msg_box.exec()

    def init_statusbar(self):
        self.statusbar = QtWidgets.QStatusBar()
        datum = strftime("%a, %d %b %Y %H:%M:%S ", gmtime())
        status_label_1 = QtWidgets.QLabel('Datum i vreme: ' + datum)
        self.statusbar.addWidget(status_label_1, 1)
        # TODO: dodati trenutno prijavljenog korinsika
        # TODO: dodati akciju <Naziv komandne akcije>
        # TODO: status <Redy>
        self.setStatusBar(self.statusbar)

    def meta_filepaht(self):
        metadata = self.putanja_fajla.split("/")
        metadata = str(metadata[-1])
        metadata = metadata.replace("_data", "_metadata.json")
        metadata = "data/" + metadata
        return metadata
