

class Magazyn:

    def __init__(self, nazwa: str, opis: str,
                 miasto: str, ilosc_pracownikow: int, rozmiar: str):
        self.nazwa = nazwa
        self.opis = opis
        self.miasto = miasto
        self.ilosc_pracownikow = ilosc_pracownikow
        self.rozmiar = rozmiar


    def __str__(self):
        return f'Magazyn {self.nazwa} {self.opis}' \
               f'w miescie {self.miasto}' \
               f'o rozmiarze {self.rozmiar}' \
               f'w ktorym pracuje {self.ilosc_pracownikow}'
