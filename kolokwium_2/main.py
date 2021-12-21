from src.dieta import Dieta
from src.dietetyk import Dietetyk
from src.pacjent import Pacjent
from src.zamowienie import Zamowienie

pacjent = Pacjent('Jan', 'Kowalski', 35, 1234)
dieta1 = Dieta('Grecka', 199.99, True, 3000)
dieta2 = Dieta('Mięsna', 399.99, False, 6000)
dietetyk = Dietetyk('Anna', 'Nowak', pacjent, dieta1)

zamowienie = Zamowienie()
zamowienie.numer_recepty = 4321
zamowienie.pacjent = pacjent
zamowienie.diety = [dieta1, dieta2]
zamowienie.dietetyk = dietetyk

print(zamowienie)

print(f'Wartość zamówienia: {zamowienie.licz_wartosc_zamowienia()}')
print(f'Ilość kalorii w zamówionych dietach: {zamowienie.licz_kalorie()}')
