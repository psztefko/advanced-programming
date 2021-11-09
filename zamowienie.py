from produkt import Produkt
from magazyn import Magazyn
from klientDetaliczny import KlientDetaliczny
from klientBiznesowy import KlientBiznesowy
import itertools


class Zamowienie:

    id_zamowienia = itertools.count().next
    produkt: Produkt
    magazyn: Magazyn
    klientDetaliczny: KlientDetaliczny
    klientBiznesowy: KlientBiznesowy

    @property
    def id_zamowienia(self):
        return self.id_zamowienia

    @property
    def produkt(self):
        return self.produkt

    @property
    def magazyn(self):
        return self.magazyn

    @property
    def klientDetaliczny(self):
        return self.klientDetaliczny

    @property
    def klientBiznesowy(self):
        return self.klientBiznesowy

    @produkt.setter
    def produkt(self, Produkt):
        self.produkt = Produkt

    @magazyn.setter
    def magazyn(self, Magazyn):
        self.Magazyn = Magazyn

    @klientDetaliczny.setter
    def klientDetaliczny(self, KlientDetaliczny):
        self.klientDetaliczny = KlientDetaliczny

    @klientBiznesowy.setter
    def klientBiznesowy(self, KlientBiznesowy):
        self.klientBiznesowy = KlientBiznesowy

    def wartosc_zamowienia(self):
        pass

    def adres_klienta(self):
        pass