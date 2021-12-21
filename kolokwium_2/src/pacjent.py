class Pacjent:

    def __init__(self, imie: str,
                 nazwisko: str,
                 wiek: int,
                 numer_pacjenta: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.numer_pacjenta = numer_pacjenta

    @property
    def imie(self) -> str:
        return self._imie

    @imie.setter
    def imie(self, imie: str):
        self._imie = imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko: str):
        self._nazwisko = nazwisko

    @property
    def wiek(self) -> int:
        return self._wiek

    @wiek.setter
    def wiek(self, wiek: int):
        self._wiek = wiek

    @property
    def numer_pacjenta(self) -> int:
        return self._numer_pacjenta

    @numer_pacjenta.setter
    def numer_pacjenta(self, numer_pacjenta: int):
        self._numer_pacjenta = numer_pacjenta

    def __str__(self) -> str:
        return f'Imie: {self._imie},\n' \
               f'Nazwisko: {self._nazwisko},\n' \
               f'Wiek: {self._wiek},\n' \
               f'Numer pacjenta: {self._numer_pacjenta}\n'
