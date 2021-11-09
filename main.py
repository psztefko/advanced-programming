from produkt import Produkt
from magazyn import Magazyn
from klientDetaliczny import KlientDetaliczny
from klientBiznesowy import KlientBiznesowy
from zamowienie import Zamowienie



if __name__ == '__main__':
    produkt1 = Produkt('zarowka',
                       'ciepla barwa', 'oswietlenie', 29.99, 1234567891234)

    produkt2 = Produkt('kabel', 'YDY-0.5',
                       'kable', 99.99, 1234567891235)

    magazyn1 = Magazyn('M1', 'magazyn glowny',
                       'Katowice', 200, 'duzy')

    klientDetaliczny1 = KlientDetaliczny('Jan', 'Kowalski',
                                         123, 'Katowice', 123123123)

    klientBiznesowy1 = KlientBiznesowy('LuxBud', 'Myslowice',
                                       'PL00111111112222222222222222', 'mail@luxbud.pl', 'wysoki')

    zamowienie1 = Zamowienie()
    zamowienie1.produkty = [produkt1, produkt2]
    zamowienie1.magazyn = magazyn1
    zamowienie1.klientDetaliczny = klientDetaliczny1

    print(zamowienie1.wartosc_zamowienia())
