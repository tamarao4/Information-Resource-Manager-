from PySide2 import QtWidgets
from handler.serial_file_handler import SerialFileHandler
from handler.sequential_file_handler import SequentialFileHandler
from model.visokoskolska_ustanova_model import VisokoskolskaUstanovaModel
from model.student_model import StudentModel
from model.studijski_program_model import StudijskiProgramModel
from model.nivo_studija_model import NivoStudijaModel
from model.nastavni_predmet_model import NastavniPredmetModel
from model.plan_studijske_grupe_model import PlanStudijskeGrupeModel
from model.tok_studija_model import TokStudijaModel


class PovezanaTabela(QtWidgets.QTableView):
    def __init__(self, glavni_model):
        super(PovezanaTabela, self).__init__()
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.glavni_model = glavni_model
        self.resizeColumnsToContents()

# tabele povezane sa ustanovom
    def ustanova_studenti(self, glavni_model):
        studenti_model = StudentModel()
        all_students = StudentModel()
        try:
            sequential_file_handler = SequentialFileHandler("data/student_data", "data/student_metadata.json")
            all_students.students = sequential_file_handler.get_all()
            for stud in all_students.students:
                stud_ustanova = str(stud.ustanova)
                glavni_model_oznaka = str(glavni_model.oznaka)
                if stud_ustanova == glavni_model_oznaka:
                    studenti_model.students.append(stud)
                    glavni_model.studenti.append(stud)
        except(Exception):
            studenti_model.students = []
        return studenti_model

    def ustanova_predmeti(self, glavni_model):
        predmet_model = NastavniPredmetModel()
        svi_predmeti = NastavniPredmetModel()
        try:
            serial_file_handler = SerialFileHandler("data/nastavni_predmet_data", "data/nastavni_predmet_metadata.json")
            svi_predmeti.nastavni_predmeti = serial_file_handler.get_all()
            for p in svi_predmeti.nastavni_predmeti:
                if str(p.ustanova) == str(glavni_model.oznaka):
                    predmet_model.nastavni_predmeti.append(p)
                    # glavni_model.predmeti.append(p)
        except(Exception):
            predmet_model.nastavni_predmeti = []
        return predmet_model

    def ustanova_st_programi(self,  glavni_model):
        st_program_model = StudijskiProgramModel()
        svi_programi = StudijskiProgramModel()
        try:
            serial_file_handler = SerialFileHandler("data/studijski_program_data", "data/studijski_program_metadata.json")
            svi_programi.studijski_programi = serial_file_handler.get_all()
            for sp in svi_programi.studijski_programi:
                if str(sp.ustanova) == str(glavni_model.oznaka):
                    st_program_model.studijski_programi.append(sp)
                    glavni_model.studijski_programi.append(sp)
        except(Exception):
            st_program_model.studijski_programi = []
        return st_program_model

# tabele povezana sa niovom studija
    def nivo_st_programi(self, glavni_model):
        st_program_model = StudijskiProgramModel()
        svi_programi = StudijskiProgramModel()
        try:
            serial_file_handler = SerialFileHandler("data/studijski_program_data", "data/studijski_program_metadata.json")
            svi_programi.studijski_programi = serial_file_handler.get_all()
            for sp in svi_programi.studijski_programi:
                if str(sp.oznaka_nivoa_studija) == str(glavni_model.oznaka):
                    st_program_model.studijski_programi.append(sp)
                    glavni_model.studijski_programi.append(sp)
        except(Exception):
            st_program_model.studijski_programi = []
        return st_program_model

# tabele povezane sa nastavnim predmetom
    def predmet_plan_st_grupe(self, glavni_model):
        st_grupe_model = PlanStudijskeGrupeModel()
        sve_st_grupe = PlanStudijskeGrupeModel()
        try:
            serial_file_handler = SerialFileHandler("data/plan_studijske_grupe_data", "data/plan_studijske_grupe_metadata.json")
            sve_st_grupe.planovi_studijskih_grupa = serial_file_handler.get_all()
            for plan in sve_st_grupe.planovi_studijskih_grupa:
                plan_iz_pedmeta = str(plan.nastavni_predmet)
                glavni_model_oznaka = str(glavni_model.oznaka)
                if plan_iz_pedmeta == glavni_model_oznaka:
                    st_grupe_model.planovi_studijskih_grupa.append(plan)
                    # glavni_model.planovi_studijske_grupe.append(plan)
        except(Exception):
            st_grupe_model.planovi_studijskih_grupa = []
        return st_grupe_model

# tabele povezane sa studijskim programom
    def st_program_plan(self, glavni_model):
        st_grupe_model = PlanStudijskeGrupeModel()
        sve_st_grupe = PlanStudijskeGrupeModel()
        try:
            serial_file_handler = SerialFileHandler("data/plan_studijske_grupe_data", "data/plan_studijske_grupe_metadata.json")
            sve_st_grupe.planovi_studijskih_grupa = serial_file_handler.get_all()
            for plan in sve_st_grupe.planovi_studijskih_grupa:
                plan_iz_programa = str(plan.studijski_program)
                glavni_model_oznaka = str(glavni_model.oznaka_programa)
                if plan_iz_programa == glavni_model_oznaka:
                    st_grupe_model.planovi_studijskih_grupa.append(plan)
                    # glavni_model.planovi_studijske_grupe.append(plan)
        except(Exception) as e:
            print(e)
        return st_grupe_model

    def st_program_tok_studija(self, glavni_model):
        tok_studija_model = TokStudijaModel()
        svi_tokovi_studija = TokStudijaModel()
        try:
            sequential_file_handler = SequentialFileHandler("data/tok_studija_data", "data/tok_studija_metadata.json")
            svi_tokovi_studija.list_tok_studija = sequential_file_handler.get_all()
            for tok in svi_tokovi_studija.list_tok_studija:
                if str(tok.oznaka_programa) == str(glavni_model.oznaka_programa):
                    tok_studija_model.list_tok_studija.append(tok)
        except(Exception):
            tok_studija_model.list_tok_studija = []
        return tok_studija_model

# tabele povezane sa studentom
    def student_tok_studija(self, glavni_model):
        tok_model = TokStudijaModel()
        svi_tokovi = TokStudijaModel()
        try:
            sequential_file_handler = SequentialFileHandler("data/tok_studija_data", "data/tok_studija_metadata.json")
            svi_tokovi.list_tok_studija = sequential_file_handler.get_all()
            for tok in svi_tokovi.list_tok_studija:
                if str(tok.student_iz_ustanove) == str(glavni_model.broj_indeksa):
                    tok_model.list_tok_studija.append(tok)
        except(Exception):
            tok_model.list_tok_studija = []
        return tok_model
