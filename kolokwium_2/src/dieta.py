class Dieta:

    def __init__(self, nazwa: str,
                 cena: float,
                 wegetarianska: bool,
                 kalorie: int):
        self.kalorie = kalorie
        self.wegetarianska = wegetarianska
        self.cena = cena
        self.nazwa = nazwa

    @property
    def nazwa(self) -> str:
        return self.nazwa

    @nazwa.setter
    def nazwa(self, nazwa: str):
        self._nazwa = nazwa

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, cena: float):
        self._cena = cena

    @property
    def kalorie(self) -> int:
        return self._kalorie

    @kalorie.setter
    def kalorie(self, kalorie: int):
        self._kalorie = kalorie

    @property
    def wegetarianska(self) -> bool:
        return self._wegetarianska

    @wegetarianska.setter
    def wegetarianska(self, wegetarianska: bool):
        self._wegetarianska = wegetarianska

    def __str__(self) -> str:
        return f'Nazwa: {self.nazwa},\n' \
               f'Cena: {self._cena},\n' \
               f'Ilość kalorii: {self._kalorie},\n' \
               f'Czy jest wegetarianska: {self._wegetarianska},\n'
