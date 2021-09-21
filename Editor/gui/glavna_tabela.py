from PySide2 import QtWidgets, QtGui, QtCore
# klasa koja trea da prikaze praznu tabelu, gde ce biti moguce unositi podatke i posle toga ih cuvati

from handler.serial_file_handler import SerialFileHandler
from handler.sequential_file_handler import SequentialFileHandler
# modeli
from model.visokoskolska_ustanova_model import VisokoskolskaUstanovaModel
from model.visokoskolska_ustavnova import VisokoskolskaUstanova
from model.student import Student
from model.student_model import StudentModel
from model.studijski_program import StudijskiProgram
from model.studijski_program_model import StudijskiProgramModel
from model.nivo_studija import NivoStudija
from model.nivo_studija_model import NivoStudijaModel
from model.nastavni_predmet import NastavniPredmet
from model.nastavni_predmet_model import NastavniPredmetModel
from model.plan_studijske_grupe import PlanStudijskeGrupe
from model.plan_studijske_grupe_model import PlanStudijskeGrupeModel
from model.tok_studija import TokStudija
from model.tok_studija_model import TokStudijaModel
# podtabele
from gui.povezana_tabela import PovezanaTabela


class GlavnaTabela(QtWidgets.QWidget):
    # ime fala koji se otvara, i on je None ako se kreira novi
    def __init__(self, file_path, pritisnuto_dugme):
        super(GlavnaTabela, self).__init__()
        self.file_path = file_path
        self.pritisnuto_dugme = pritisnuto_dugme
        self.main_layout = QtWidgets.QVBoxLayout()
        self.create_tab_widget()
        # za akcije dodavanja i brisanje reda

        # -------------------
        self.icon = QtGui.QIcon("res/icons8-edit-file-64.png")

        # ------------------------
        try:
            self.metadata = self.file_path.split("/")
            self.metadata = self.metadata[-1].replace("_data", "_metadata.json")
            self.metadata = "data/" + self.metadata
            self.serial_file_handler = SerialFileHandler(self.file_path, self.metadata)
            self.sequential_file_handler = SequentialFileHandler(self.file_path, self.metadata)
        except Exception:
            pass

        # ----------------------
        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.vs_model = self.ucitavanje_model()
        self.table1.clicked.connect(self.dodavanje_reda)
        self.table1.clicked.connect(self.brisanje_reda)

        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

        self.table1.resizeColumnsToContents()

    def create_table(self, rows, columns):
        table_widget = QtWidgets.QTableWidget(rows, columns, self)
        return table_widget

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabsClosable(True)   # kako da zatvorim tab ????
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def ucitavanje_model(self):
        metadata = self.file_path.split("/")
        metadata = metadata[-1]
        if (metadata == "visokoskolska_ustanova_data"):
            self.ucitavanje_vs_ustanova()
        elif (metadata == "student_data"):
            self.ucitavanje_studenata()
        elif (metadata == "studijski_program_data"):
            self.ucitavanje_studijkish_programa()
        elif (metadata == "nivo_studija_data"):
            self.ucitavanje_nivoa_studija()
        elif (metadata == "nastavni_predmet_data"):
            self.ucitavanje_nastavnih_predmeta()
        elif (metadata == "plan_studijske_grupe_data"):
            self.ucitavnje_plana()
        elif (metadata == "tok_studija_data"):
            self.ucitavanje_toka_studija()
        else:
            self.table1 = self.create_table(1, 1)
            print("Nije ucitan ni jedan model.")

    def ucitavanje_vs_ustanova(self):
        vs_model = VisokoskolskaUstanovaModel()
        # deo fje koji nam treba, koji ucitava iz serijsk dat i kreira st_mo
        vs_model.visokoskolske_ustanove = self.serial_file_handler.get_all()
        if vs_model.visokoskolske_ustanove == []:
            vs_model.visokoskolske_ustanove.append(VisokoskolskaUstanova('', '', '', [], [], []))

        # upisujem poslednj id, zbog automatizacije id-a
        id = vs_model.visokoskolske_ustanove[-1].oznaka
        if id == "":
            id = "0"
        f = open("id.txt", 'w')
        f.write(id)

        self.table1.setModel(vs_model)
        # na klik pirkazuje povezane tabele
        self.table1.clicked.connect(self.ustanova_selected)

    def ustanova_selected(self, index):
        # ovde otvaram sve povezane tabele sa ustanovom
        model = self.table1.model()
        vs_ustanova = model.get_element(index)
        self.tab_widget.clear()
        # studenti
        self.subtable1 = PovezanaTabela(self)
        studenti_model = PovezanaTabela.ustanova_studenti(self, vs_ustanova)
        self.subtable1.setModel(studenti_model)
        self.tab_widget.addTab(self.subtable1, self.icon, "Studenti")
        #  nastavni predmeti
        self.subtable2 = PovezanaTabela(self)
        predmet_model = PovezanaTabela.ustanova_predmeti(self, vs_ustanova)
        self.subtable2.setModel(predmet_model)
        self.tab_widget.addTab(self.subtable2, self.icon, "Nastani predmeti")
        # studijski programi
        self.subtable3 = PovezanaTabela(self)
        sp_model = PovezanaTabela.ustanova_st_programi(self, vs_ustanova)
        self.subtable3.setModel(sp_model)
        self.tab_widget.addTab(self.subtable3, self.icon, "Studijski programi")

    def ucitavanje_studenata(self):
        studenti_model = StudentModel()
        studenti_model.students = self.sequential_file_handler.get_all()
        if studenti_model.students == []:
            studenti_model.students.append(Student('', '', '', '', '', '', '', '', '', '', '', []))

        # upisujem poslednj id, zbog automatizacije id-a
        id = studenti_model.students[-1].broj_indeksa
        if id == "":
            id = "0"
        f = open("id.txt", 'w')
        f.write(id)

        self.table1.setModel(studenti_model)
        self.table1.clicked.connect(self.student_selected)

    def student_selected(self, index):
        model = self.table1.model()
        student = model.get_element(index)
        self.tab_widget.clear()
        # tokovi studija
        self.subtable1 = PovezanaTabela(self)
        tok_studija_model = PovezanaTabela.student_tok_studija(self, student)
        self.subtable1.setModel(tok_studija_model)
        self.tab_widget.addTab(self.subtable1, self.icon, "Tok studija")

    def ucitavanje_studijkish_programa(self):
        sp_model = StudijskiProgramModel()
        sp_model.studijski_programi = self.serial_file_handler.get_all()
        if sp_model.studijski_programi == []:
            sp_model.studijski_programi.append(StudijskiProgram('', '', '', '', []))

        # upisujem poslednj id, zbog automatizacije id-a
        id = sp_model.studijski_programi[-1].oznaka_programa
        if id == "":
            id = "0"
        f = open("id.txt", 'w')
        f.write(id)

        self.table1.setModel(sp_model)
        self.table1.clicked.connect(self.st_program_selected)

    def st_program_selected(self, index):
        model = self.table1.model()
        st_program = model.get_element(index)
        self.tab_widget.clear()
        # plans studijske grupe
        self.subtable1 = PovezanaTabela(self)
        plan_model = PovezanaTabela.st_program_plan(self, st_program)
        self.subtable1.setModel(plan_model)
        self.tab_widget.addTab(self.subtable1, self.icon, "Plan studijske grupe")
        #  tok studija
        self.subtable2 = PovezanaTabela(self)
        tok_studija_model = PovezanaTabela.st_program_tok_studija(self, st_program)
        self.subtable2.setModel(tok_studija_model)
        self.tab_widget.addTab(self.subtable2, self.icon, "Ko studira")

    def ucitavanje_nivoa_studija(self):
        ns_model = NivoStudijaModel()
        ns_model.nivoi_studija = self.serial_file_handler.get_all()
        if ns_model.nivoi_studija == []:
            ns_model.nivoi_studija.append(NivoStudija('', '', []))

        # upisujem poslednj id, zbog automatizacije id-a
        id = ns_model.nivoi_studija[-1].oznaka
        if id == "":
            id = "0"
        f = open("id.txt", 'w')
        f.write(id)

        self.table1.setModel(ns_model)
        self.table1.clicked.connect(self.nivo_studija_selected)

    def nivo_studija_selected(self, index):
        model = self.table1.model()
        nivo_studija = model.get_element(index)
        self.tab_widget.clear()
        # studijski programi
        self.subtable1 = PovezanaTabela(self)
        programi_model = PovezanaTabela.nivo_st_programi(self, nivo_studija)
        self.subtable1.setModel(programi_model)
        self.tab_widget.addTab(self.subtable1, self.icon, "Studijski programi")

    def ucitavanje_nastavnih_predmeta(self):
        np_model = NastavniPredmetModel()
        np_model.nastavni_predmeti = self.serial_file_handler.get_all()
        if np_model.nastavni_predmeti == []:
            np_model.nastavni_predmeti.append(NastavniPredmet('', '', '', '', [], []))
        self.table1.setModel(np_model)

        # upisujem poslednj id, zbog automatizacije id-a
        id = np_model.nastavni_predmeti[-1].oznaka
        if id == "":
            id = "0"
        f = open("id.txt", 'w')
        f.write(id)

        # na klik pirkazuje povezane tabele
        self.table1.clicked.connect(self.predmet_selected)

    def predmet_selected(self, index):
        model = self.table1.model()
        predmet = model.get_element(index)
        self.tab_widget.clear()
        # studijski programi
        self.subtable = PovezanaTabela(self)
        plan_model = PovezanaTabela.predmet_plan_st_grupe(self, predmet)
        self.subtable.setModel(plan_model)
        self.tab_widget.addTab(self.subtable, self.icon, "Plan studijske gurpe")

    def ucitavnje_plana(self):
        plan_model = PlanStudijskeGrupeModel()
        plan_model.planovi_studijskih_grupa = self.serial_file_handler.get_all()
        if plan_model.planovi_studijskih_grupa == []:
            plan_model.planovi_studijskih_grupa.append(PlanStudijskeGrupe('', '', '', '', '', ''))

        # upisujem poslednj id, zbog automatizacije id-a
        id = plan_model.planovi_studijskih_grupa[-1].oznaka
        if id == "":
            id = "0"
        f = open("id.txt", 'w')
        f.write(id)

        self.table1.setModel(plan_model)

    def ucitavanje_toka_studija(self):
        tok_studija_model = TokStudijaModel()
        tok_studija_model.list_tok_studija = self.sequential_file_handler.get_all()
        if tok_studija_model.list_tok_studija == []:
            tok_studija_model.list_tok_studija.append(TokStudija('', '', '', '', '', '', '', '', '', '', '', '', ''))

        # upisujem poslednj id, zbog automatizacije id-a
        id = tok_studija_model.list_tok_studija[-1].br_upisa
        if id == "":
            id = "0"
        f = open("id.txt", 'w')
        f.write(id)

        self.table1.setModel(tok_studija_model)

    # -------------------------------------------------------------------

    def dodavanje_reda(self, index):
        if self.pritisnuto_dugme == 1:
            model = self.table1.model()
            br_redova = model.rowCount(index)
            self.pritisnuto_dugme = 0
            model.insertRows(br_redova, 1, QtCore.QModelIndex())

    def brisanje_reda(self, index):
        if self.pritisnuto_dugme == 2:
            model = self.table1.model()
            print(self.pritisnuto_dugme)
            self.pritisnuto_dugme = 0
            model.removeRows(index.row(), 1, QtCore.QModelIndex())
