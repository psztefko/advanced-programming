from kolokwium_2.src.dieta import Dieta
from kolokwium_2.src.pacjent import Pacjent


class Dietetyk:

    def __init__(self, imie: str,
                 nazwisko: str,
                 pacjent: Pacjent,
                 dieta: Dieta):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pacjent = pacjent
        self.dieta = dieta

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
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent):
        self._pacjent = pacjent

    @property
    def dieta(self) -> Dieta:
        return self._dieta

    @dieta.setter
    def dieta(self, dieta: Dieta):
        self._dieta = dieta

    def __str__(self) -> str:
        return f'Imie: {self._imie},\n' \
               f'Nazwisko: {self._nazwisko},\n' \
               f'Pacjent: {self._pacjent.imie},\n' \
               f'Dieta: {self._dieta.nazwa},\n'
