from PySide2 import QtCore, QtGui
from model.student import Student
from handler.sequential_file_handler import SequentialFileHandler
from PySide2.QtCore import QModelIndex


class StudentModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.students = []  # ovo je osnovna lista modela
        self.sequential_file_handler = SequentialFileHandler('data/student_data', 'data/student_metadata.json')

    def get_element(self, index):
        # vratiti studenta na datom redu
        return self.students[index.row()]

    # metode za redefisanje read-only modela
    def rowCount(self, index):
        # + 1 zato jer za dodavanje ostavljam jedan prazan red
        return len(self.students)

    def columnCount(self, index):
        return 11  # zbog broja atributa koje prikazujemo o studentu

    def data(self, index, role=QtCore.Qt.DisplayRole):
        student = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return student.broj_indeksa
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return student.struka
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return student.ustanova
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return student.prezime
        elif index.column() == 4 and role == QtCore.Qt.DisplayRole:
            return student.ime_roditelja
        elif index.column() == 5 and role == QtCore.Qt.DisplayRole:
            return student.ime
        elif index.column() == 6 and role == QtCore.Qt.DisplayRole:
            return student.pol
        elif index.column() == 7 and role == QtCore.Qt.DisplayRole:
            return student.adresa_stanovanja
        elif index.column() == 8 and role == QtCore.Qt.DisplayRole:
            return student.telefon
        elif index.column() == 9 and role == QtCore.Qt.DisplayRole:
            return student.jmbg
        elif index.column() == 10 and role == QtCore.Qt.DisplayRole:
            return student.datum_rodjenja
        if index.column() == 0 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(158, 196, 240))
        if role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(227, 236, 246))

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj indeksa"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Struka"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ustanova"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Prezime"
        elif section == 4 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ime roditelja"
        elif section == 5 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ime"
        elif section == 6 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Pol"
        elif section == 7 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Adresa stanovanja"
        elif section == 8 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Telefon"
        elif section == 9 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "JMBG"
        elif section == 10 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Datum rodjenja"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        student = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            student.broj_indeksa = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            student.struka = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            student.ustanova = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole:
            student.prezime = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 4 and role == QtCore.Qt.EditRole:
            student.ime_roditelja = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 5 and role == QtCore.Qt.EditRole:
            student.ime = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 6 and role == QtCore.Qt.EditRole:
            student.pol = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 7 and role == QtCore.Qt.EditRole:
            student.adresa_stanovanja = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 8 and role == QtCore.Qt.EditRole:
            student.telefon = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 9 and role == QtCore.Qt.EditRole:
            student.jmbg = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        elif index.column() == 10 and role == QtCore.Qt.EditRole:
            student.datum_rodjenja = value
            self.sequential_file_handler.edit(student.broj_indeksa, student)
            return True
        return False

    def flags(self, index):
        if index.column() == 0:
            return ~QtCore.Qt.ItemIsEditable
        return super().flags(index) | QtCore.Qt.ItemIsEditable

    def insertRows(self, row, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), row, row + rows - 1)
        f = open("id.txt", "r")
        id = f.read()
        novi_id = id.replace("270", "")
        novi_id = int(novi_id) + 1
        novi_id = "270" + str(novi_id)
        for row in range(rows):
            novi_student = Student(novi_id, '', '', '', '', '', '', '', '', '', '', [])
            self.students.insert(row + row, novi_student)
            self.sequential_file_handler.insert(novi_student)
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        i = self.students[row]
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        self.students = self.students[:row] + self.students[row + rows:]
        self.sequential_file_handler.delete_one(str(i.broj_indeksa))
        self.endRemoveRows()
        return True
