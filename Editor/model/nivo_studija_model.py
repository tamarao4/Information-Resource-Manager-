from PySide2 import QtCore, QtGui
from model.nivo_studija import NivoStudija
from handler.serial_file_handler import SerialFileHandler
from PySide2.QtCore import QModelIndex


class NivoStudijaModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # osnovna lista modela
        self.nivoi_studija = []
        self.serial_file_handler = SerialFileHandler("data/nivo_studija_data", "data/nivo_studija_metadata.json")

    def get_element(self, index):
        # vrati element na datom red
        return self.nivoi_studija[index.row()]

    def rowCount(self, index):
        return len(self.nivoi_studija)

    def columnCount(self, index):
        # zbog broja atributa koje prikazujemo
        return 2

    def data(self, index, role=QtCore.Qt.DisplayRole):
        nivo = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return nivo.oznaka
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return nivo.naziv
        if index.column() == 0 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtCore.Qt.lightGray)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Oznaka"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        nivo = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            nivo.oznaka = value
            ns = NivoStudija(value, nivo.naziv)
            self.serial_file_handler.edit(ns.oznaka, ns)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            nivo.naziv = value
            ns = NivoStudija(nivo.oznaka, value)
            self.serial_file_handler.edit(ns.oznaka, ns)
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
        novi_id = id.replace("nstud", "")
        novi_id = int(novi_id) + 1
        novi_id = "nstud" + str(novi_id)
        for row in range(rows):
            ns = NivoStudija(novi_id, '', [])
            self.nivoi_studija.insert(row + row, ns)
            self.serial_file_handler.insert(ns)
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        i = self.nivoi_studija[row]
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        self.nivoi_studija = self.nivoi_studija[:row] + self.nivoi_studija[row + rows:]
        self.serial_file_handler.delete_one(str(i.oznaka))
        self.endRemoveRows()
        return True
