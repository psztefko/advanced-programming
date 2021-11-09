

class KlientBiznesowy:

    def __init__(self, nazwa: str, lokalizacja: str, iban: str, mail: str, priorytet: str):
        self.nazwa = nazwa
        self.lokalizacja = lokalizacja
        self.iban = iban
        self.mail = mail
        self.priorytet = priorytet

    def __str__(self):
        return f'Klient {self.nazwa}' \
               f'z miasta {self.lokalizacja}' \
               f'o numerze iban {self.iban}' \
               f'mailu {self.mail}' \
               f'oraz priorytecie {self.priorytet}'
