

class KlientDetaliczny:

    def __init__(self, imie: str, nazwisko: str,
                 numer_klienta: int, miasto: str, numer_telefonu: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_klienta = numer_klienta
        self.miasto = miasto
        self.numer_telefonu = numer_telefonu

    def __str__(self):
        return f'Klient {self.imie} {self.nazwisko}' \
               f'z miasta {self.miasto}' \
               f'o numerze telefonu {self.numer_telefonu}' \
               f'oraz numerze klienta {self.numer_klienta}'
