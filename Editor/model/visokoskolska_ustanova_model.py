from PySide2 import QtCore, QtGui
from model.visokoskolska_ustavnova import VisokoskolskaUstanova
from handler.serial_file_handler import SerialFileHandler
from PySide2.QtCore import QModelIndex


class VisokoskolskaUstanovaModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # osnovna lista modela
        self.visokoskolske_ustanove = []
        self.serial_file_handler = SerialFileHandler("data/visokoskolska_ustanova_data", "data/visokoskolska_ustanova_metadata.json")

    def get_element(self, index):
        # vrati element na datom red
        return self.visokoskolske_ustanove[index.row()]

    def rowCount(self, index):
        return len(self.visokoskolske_ustanove)

    def columnCount(self, index):
        # zbog broja atributa koje prikazujemo
        return 3

    def data(self, index, role=QtCore.Qt.DisplayRole):
        visokoskolska_ustanova = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return visokoskolska_ustanova.oznaka
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return visokoskolska_ustanova.naziv
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return visokoskolska_ustanova.adresa
        if index.column() == 0 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtCore.Qt.lightGray)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Oznaka"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Adresa"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        visokoskolska_ustavnova = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            return False
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            visokoskolska_ustavnova.naziv = value
            vs = VisokoskolskaUstanova(visokoskolska_ustavnova.oznaka, value, visokoskolska_ustavnova.adresa)
            self.serial_file_handler.edit(vs.oznaka, vs)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            visokoskolska_ustavnova.adresa = value
            vs = VisokoskolskaUstanova(visokoskolska_ustavnova.oznaka, visokoskolska_ustavnova.naziv, value)
            self.serial_file_handler.edit(vs.oznaka, vs)
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
        novi_id = id.replace("vsu", "")
        novi_id = int(novi_id) + 1
        novi_id = "vsu" + str(novi_id)
        # prikaz novog reda
        for row in range(rows):
            vs = VisokoskolskaUstanova(novi_id, '', '', [], [], [])
            self.visokoskolske_ustanove.insert(row + row, vs)
            self.serial_file_handler.insert(vs)
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        i = self.visokoskolske_ustanove[row]
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        self.visokoskolske_ustanove = self.visokoskolske_ustanove[:row] + self.visokoskolske_ustanove[row + rows:]
        self.serial_file_handler.delete_one(str(i.oznaka))
        self.endRemoveRows()
        return True
