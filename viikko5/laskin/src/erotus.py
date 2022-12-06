class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovelluslogiikka.miinus(self.lue_syote())

    def kumoa(self):
        self.sovelluslogiikka.plus(self.lue_syote())
