from PySide2 import QtCore, QtGui
from model.plan_studijske_grupe import PlanStudijskeGrupe
from handler.serial_file_handler import SerialFileHandler
from PySide2.QtCore import QModelIndex


class PlanStudijskeGrupeModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.planovi_studijskih_grupa = []  # ovo je osnovna lista modela'
        self.serial_file_handler = SerialFileHandler("data/plan_studijske_grupe_data", "data/plan_studijske_grupe_metadata.json")

    def get_element(self, index):
        return self.planovi_studijskih_grupa[index.row()]

    def rowCount(self, index):
        return len(self.planovi_studijskih_grupa)

    def columnCount(self, index):
        return 6  # zbog broja atributa koje prikazujemo o planu

    def data(self, index, role=QtCore.Qt.DisplayRole):
        plan = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return plan.oznaka
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return plan.studijski_program
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return plan.nastavni_predmet
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return plan.blok
        elif index.column() == 4 and role == QtCore.Qt.DisplayRole:
            return plan.pozicija
        elif index.column() == 5 and role == QtCore.Qt.DisplayRole:
            return plan.ustanova_predmet
        if index.column() == 0 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtCore.Qt.lightGray)
        if index.column() == 1 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(239, 239, 241))
        if index.column() == 2 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(239, 239, 241))
        if index.column() == 5 and role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(239, 239, 241))

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Oznaka modela"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Studijski program"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Nastavni predmet"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Blok"
        elif section == 4 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Pozicija"
        elif section == 5 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ustanova predmet"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        plan = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            plan.oznaka = value
            self.serial_file_handler.edit(plan.oznaka, plan)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            plan.studijski_program = value
            self.serial_file_handler.edit(plan.oznaka, plan)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            plan.nastavni_predmet = value
            self.serial_file_handler.edit(plan.oznaka, plan)
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole:
            plan.blok = value
            self.serial_file_handler.edit(plan.oznaka, plan)
            return True
        elif index.column() == 4 and role == QtCore.Qt.EditRole:
            plan.pozicija = value
            self.serial_file_handler.edit(plan.oznaka, plan)
            return True
        elif index.column() == 5 and role == QtCore.Qt.EditRole:
            plan.ustanova_predmet = value
            self.serial_file_handler.edit(plan.oznaka, plan)
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
        novi_id = id.replace("sg", "")
        novi_id = int(novi_id) + 1
        novi_id = "sg" + str(novi_id)

        for row in range(rows):
            novi_plan = PlanStudijskeGrupe(novi_id, '', '', '', '', '')
            self.planovi_studijskih_grupa.insert(row + row, novi_plan)
            self.serial_file_handler.insert(novi_plan)
        self.endInsertRows()
        return True

    def removeRows(self, row, rows=1, index=QModelIndex()):
        # trenutno brise samo iz prikaza
        plan = self.planovi_studijskih_grupa[row]
        self.beginRemoveRows(QModelIndex(), row, row + rows - 1)
        self.planovi_studijskih_grupa = self.planovi_studijskih_grupa[:row] + self.planovi_studijskih_grupa[row + rows:]
        self.serial_file_handler.delete_one(str(plan.oznaka))
        self.endRemoveRows()
        return True
