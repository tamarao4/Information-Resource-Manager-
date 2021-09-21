from PySide2 import QtCore, QtGui
from model.nastavni_predmet import NastavniPredmet
from handler.serial_file_handler import SerialFileHandler
from PySide2.QtCore import QModelIndex


class NastavniPredmetModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # osnovna lista modela
        self.nastavni_predmeti = []
        self.serial_file_handler = SerialFileHandler("data/nastavni_predmet_data", "data/nastavni_predmet_metadata.json")

    def get_element(self, index):
        # vrati element na datom red
        return self.nastavni_predmeti[index.row()]

    def rowCount(self, index):
        return len(self.nastavni_predmeti)

    def columnCount(self, index):
        # zbog broja atributa koje prikazujemo
        return 4

    def data(self, index, role=QtCore.Qt.DisplayRole):
        predmet = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return predmet.oznaka
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return predmet.ustanova
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return predmet.naziv
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return predmet.espb
        if index.column() == 0 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtCore.Qt.lightGray)
        if index.column() == 1 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(239, 239, 241))

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Oznaka"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ustanova"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj ESPB bodova"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        predmet = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            predmet.oznaka = value
            self.serial_file_handler.edit(predmet.oznaka, predmet)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            predmet.ustanova = value
            self.serial_file_handler.edit(predmet.oznaka, predmet)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            predmet.naziv = value
            self.serial_file_handler.edit(predmet.oznaka, predmet)
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole:
            predmet.espb = value
            self.serial_file_handler.edit(predmet.oznaka, predmet)
            return True
        return False

    def flags(self, index):
        if index.column() == 0:
            return ~QtCore.Qt.ItemIsEditable
        return super().flags(index) | QtCore.Qt.ItemIsEditable

    def insertRows(self, row, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), row, row + rows - 1)
        # automatizaciija id-a
        f = open("id.txt", "r")
        id = f.read()
        novi_id = id.replace("nst", "")
        novi_id = int(novi_id) + 1
        novi_id = "nst" + str(novi_id)

        for row in range(rows):
            p = NastavniPredmet(novi_id, '', '', [], [], [])
            self.nastavni_predmeti.insert(row + row, p)
            self.serial_file_handler.insert(p)
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        i = self.nastavni_predmeti[row]
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        self.nastavni_predmeti = self.nastavni_predmeti[:row] + self.nastavni_predmeti[row + rows:]
        self.serial_file_handler.delete_one(str(i.oznaka))
        self.endRemoveRows()
        return True
