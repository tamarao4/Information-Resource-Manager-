from PySide2 import QtCore, QtGui
from model.studijski_program import StudijskiProgram
from handler.serial_file_handler import SerialFileHandler
from PySide2.QtCore import QModelIndex


class StudijskiProgramModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # osnovna lista modela
        self.studijski_programi = []
        self.serial_file_handler = SerialFileHandler("data/studijski_program_data", "data/studijski_program_metadata.json")

    def get_element(self, index):
        # vrati element na datom red
        return self.studijski_programi[index.row()]

    def rowCount(self, index):
        return len(self.studijski_programi)

    def columnCount(self, index):
        # zbog broja atributa koje prikazujemo
        return 4

    def data(self, index, role=QtCore.Qt.DisplayRole):
        studijski_program = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return studijski_program.oznaka_programa
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return studijski_program.ustanova
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return studijski_program.oznaka_nivoa_studija
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return studijski_program.naziv_programa
        if index.column() == 0 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtCore.Qt.lightGray)
        if index.column() == 1 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(239, 239, 241))
        if index.column() == 2 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(239, 239, 241))

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Oznaka programa"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ustanova"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Oznaka nivoa"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv programa"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        studijski_program = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            studijski_program.oznaka_programa = value
            sp = StudijskiProgram(value, studijski_program.ustanova, studijski_program.oznaka_nivoa_studija, studijski_program.naziv_programa)
            self.serial_file_handler.edit(sp.oznaka_programa, sp)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            studijski_program.ustanova = value
            sp = StudijskiProgram(studijski_program.oznaka_programa, value, studijski_program.oznaka_nivoa_studija, studijski_program.naziv_programa)
            self.serial_file_handler.edit(sp.oznaka_programa, sp)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            studijski_program.oznaka_nivoa_studija = value
            sp = StudijskiProgram(studijski_program.oznaka_programa, studijski_program.ustanova, value, studijski_program.naziv_programa)
            self.serial_file_handler.edit(sp.oznaka_programa, sp)
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole:
            studijski_program.naziv_programa = value
            sp = StudijskiProgram(studijski_program.oznaka_programa, studijski_program.ustanova, studijski_program.oznaka_nivoa_studija, value)
            self.serial_file_handler.edit(sp.oznaka_programa, sp)
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
        novi_id = id.replace("sp", "")
        novi_id = int(novi_id) + 1
        novi_id = "sp " + str(novi_id)
        for row in range(rows):
            sp = StudijskiProgram(novi_id, '', '', '', [])
            self.studijski_programi.insert(row + row, sp)
            self.serial_file_handler.insert(sp)
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        i = self.studijski_programi[row]
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        self.studijski_programi = self.studijski_programi[:row] + self.studijski_programi[row + rows:]
        self.serial_file_handler.delete_one(str(i.oznaka_programa))
        self.endRemoveRows()
        return True
