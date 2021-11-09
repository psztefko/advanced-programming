
class Produkt:

    def __init__(self, nazwa: str, opis: str, kategoria: str, cena: float, ean: int):
        self.nazwa = nazwa
        self.opis = opis
        self.kategoria = kategoria
        self.cena = cena
        self.ean = ean


    def __str__(self):
        return f'Produkt {self.nazwa} {self.opis}' \
               f'z kategorii {self.kategoria} ' \
               f'kosztujacy {self.cena} zlotych' \
               f'majacy kod ean {self.ean}'
