from typing import List

from kolokwium_2.src.dieta import Dieta
from kolokwium_2.src.dietetyk import Dietetyk
from kolokwium_2.src.pacjent import Pacjent


class Zamowienie:

    @property
    def numer_recepty(self) -> int:
        return self._numer_recepty

    @numer_recepty.setter
    def numer_recepty(self, numer_recepty: int):
        self._numer_recepty = numer_recepty

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent):
        self._pacjent = pacjent

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, dietetyk: Dietetyk):
        self._dietetyk = dietetyk

    @property
    def diety(self) -> List[Dieta]:
        return self._diety

    @diety.setter
    def diety(self, diety: List[Dieta]):
        self._diety = diety

    def licz_wartosc_zamowienia(self) -> float:
        return round(sum(dieta.cena
                         for dieta in self._diety), 2)

    def licz_kalorie(self) -> float:
        return round(sum(dieta.kalorie
                         for dieta in self._diety), 2)

    def __str__(self) -> str:
        return f'Numer recepty: {self._numer_recepty},\n' \
               f'Pacjent: \n{self._pacjent},\n' \
               f'Dietetyk: \n{self._dietetyk},\n' \
               #f'Diety: \n'.join(str(dieta) for dieta in self.diety)
