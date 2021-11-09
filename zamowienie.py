from produkt import Produkt
from magazyn import Magazyn
from klientDetaliczny import KlientDetaliczny
from klientBiznesowy import KlientBiznesowy


class Zamowienie:

    __produkt: Produkt
    __magazyn: Magazyn
    __klientDetaliczny: KlientDetaliczny
    __klientBiznesowy: KlientBiznesowy
    __produkty = []


    @property
    def id_zamowienia(self):
        return self.__id_zamowienia

    @property
    def produkty(self):
        return self.__produkty

    @property
    def magazyn(self):
        return self.__magazyn

    @property
    def klientDetaliczny(self):
        return self.__klientDetaliczny

    @property
    def klientBiznesowy(self):
        return self.__klientBiznesowy

    @id_zamowienia.setter
    def id_zamowienia(self, id_zamowienia):
        self.__id_zamowienia = id_zamowienia

    @produkty.setter
    def produkty(self, Produkt):
        self.__produkt = Produkt
        self.__produkty.append(Produkt)

    @magazyn.setter
    def magazyn(self, Magazyn):
        self.__magazyn = Magazyn

    @klientDetaliczny.setter
    def klientDetaliczny(self, KlientDetaliczny):
        self.__klientDetaliczny = KlientDetaliczny

    @klientBiznesowy.setter
    def klientBiznesowy(self, KlientBiznesowy):
        self.__klientBiznesowy = KlientBiznesowy

    def wartosc_zamowienia(self) -> float:
        razem = 0
        for produkt in self.__produkty:
            razem += produkt.cena
        return "{:.2f}".format(razem)

    def adres_klienta(self) -> str:
        if self.__klientBiznesowy is not None:
            return self.klientBiznesowy.lokalizacja
        elif self.__klientDetaliczny is not None:
            return self.__klientDetaliczny.miasto

    def __str__(self):
        return f'Nie zdazylem'
