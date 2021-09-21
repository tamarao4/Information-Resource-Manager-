class VisokoskolskaUstanova():
    def __init__(self, oznaka, naziv, adresa, studenti=[], predmeti=[], studijski_programi=[]):
        self.oznaka = oznaka
        self.naziv = naziv
        self.adresa = adresa
        self.studenti = studenti
        self.predmeti = predmeti
        self.studijski_programi = studijski_programi
        '''
        negde u programu se pravi dodatna prazna lista i ne prepoznaje se atribut posle adrese,
        zbog toga sam dodala jos jednu lisu koju nigde ne koristim,
        ali kasnije mogu da radim sa sudenti_lista
        tako sto to koristim za povezivanje tabela
        '''
