from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostos_lista = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        return sum([self.ostos_lista[ostos].lukumaara() for ostos in self.ostos_lista])

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return sum([self.ostos_lista[ostos].hinta() for ostos in self.ostos_lista])

    def lisaa_tuote(self, lisattava: Tuote):
        nimi = lisattava.nimi()
        if nimi in self.ostos_lista:
            self.ostos_lista[nimi].muuta_lukumaaraa(1)
        else:
            self.ostos_lista[nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        nimi = poistettava.nimi()
        if nimi in self.ostos_lista:
            self.ostos_lista[nimi].muuta_lukumaaraa(-1)
            if self.ostos_lista[nimi].lukumaara() == 0:
                del self.ostos_lista[nimi]


    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostos_lista = {}

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return list(self.ostos_lista.values())

