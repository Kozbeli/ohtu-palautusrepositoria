import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.viitegeneraattori_mock.uusi.return_value = 99

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5
            elif tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "kahvi", 3)
            elif tuote_id == 3:
                return Tuote(3, "suklaa", 2)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa.aloita_asiointi()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # varmistetaan, että tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 99, "12345", ANY, 5)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikein_kahdella_eri_tuotteella(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 99, "12345", ANY, 8)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikein_kahdella_samalla_tuotteella(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 99, "12345", ANY, 10)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikein_kahdella_eri_tuotteella_josta_toinen_on_loppu(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 99, "12345", ANY, 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 99, "12345", ANY, 5)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 3)

    def test_korista_poistaminen_toimii(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 3)
