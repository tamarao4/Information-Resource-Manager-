from PySide2 import QtCore, QtGui
from model.tok_studija import TokStudija
from handler.sequential_file_handler import SequentialFileHandler
from PySide2.QtCore import QModelIndex


class TokStudijaModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_tok_studija = []  # ovo je osnovna lista modela
        self.sequential_file_handler = SequentialFileHandler('data/tok_studija_data', 'data/tok_studija_metadata.json')

    def get_element(self, index):
        # vratiti studenta na datom redu
        return self.list_tok_studija[index.row()]

    # metode za redefisanje read-only modela
    def rowCount(self, index):
        # + 1 zato jer za dodavanje ostavljam jedan prazan red
        return len(self.list_tok_studija)

    def columnCount(self, index):
        return 13

    def data(self, index, role=QtCore.Qt.DisplayRole):
        tok_studija = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return tok_studija.br_upisa
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return tok_studija.ustanova
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return tok_studija.oznaka_programa
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return tok_studija.student_iz_ustanove
        elif index.column() == 4 and role == QtCore.Qt.DisplayRole:
            return tok_studija.struka
        elif index.column() == 5 and role == QtCore.Qt.DisplayRole:
            return tok_studija.broj_indeksa
        elif index.column() == 6 and role == QtCore.Qt.DisplayRole:
            return tok_studija.skolska_godina
        elif index.column() == 7 and role == QtCore.Qt.DisplayRole:
            return tok_studija.godina_studija
        elif index.column() == 8 and role == QtCore.Qt.DisplayRole:
            return tok_studija.blok
        elif index.column() == 9 and role == QtCore.Qt.DisplayRole:
            return tok_studija.datum_upisa
        elif index.column() == 10 and role == QtCore.Qt.DisplayRole:
            return tok_studija.datum_overe
        elif index.column() == 11 and role == QtCore.Qt.DisplayRole:
            return tok_studija.espb_pocetni
        elif index.column() == 12 and role == QtCore.Qt.DisplayRole:
            return tok_studija.espb_krajnji
        if index.column() == 0 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(158, 196, 240))
        if role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(227, 236, 246))

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj upisa"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ustanova"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Oznaka programa"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Student iz ustanove"
        elif section == 4 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Struka"
        elif section == 5 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj indeksa"
        elif section == 6 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Skolska godina"
        elif section == 7 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Godina studija"
        elif section == 8 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Blok"
        elif section == 9 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Datum upisa"
        elif section == 10 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Datum overe"
        elif section == 11 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "ESPB pocetni"
        elif section == 12 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "ESPB krajnji"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        tok_studija = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            tok_studija.br_upisa = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            tok_studija.ustanova = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            tok_studija.oznaka_programa = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole:
            tok_studija.student_iz_ustanove = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 4 and role == QtCore.Qt.EditRole:
            tok_studija.struka = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 5 and role == QtCore.Qt.EditRole:
            tok_studija.broj_indeksa = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 6 and role == QtCore.Qt.EditRole:
            tok_studija.skolska_godina = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 7 and role == QtCore.Qt.EditRole:
            tok_studija.godina_studija = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 8 and role == QtCore.Qt.EditRole:
            tok_studija.blok = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 9 and role == QtCore.Qt.EditRole:
            tok_studija.datum_upisa = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 10 and role == QtCore.Qt.EditRole:
            tok_studija.datum_overe = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 11 and role == QtCore.Qt.EditRole:
            tok_studija.espb_pocetni = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
            return True
        elif index.column() == 12 and role == QtCore.Qt.EditRole:
            tok_studija.espb_krajnji = value
            self.sequential_file_handler.edit(tok_studija.br_upisa, tok_studija)
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
        novi_id = id.replace("br", "")
        novi_id = int(novi_id) + 1
        novi_id = str(novi_id)

        for row in range(rows):
            novi = TokStudija(novi_id, '', '', '', '', '', '', '', '', '', '', '', '')
            self.list_tok_studija.insert(row + row, novi)
            self.sequential_file_handler.insert(novi)
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        i = self.list_tok_studija[row]
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        self.list_tok_studija = self.list_tok_studija[:row] + self.list_tok_studija[row + rows:]
        self.sequential_file_handler.delete_one(str(i.br_upisa))
        self.endRemoveRows()
        return True
