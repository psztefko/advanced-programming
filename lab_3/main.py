

def func_1(name: str, surname: str) -> str:
    return f'Cześć {name} {surname}!'

def func_2(num1: int, num2: int) -> int:
    return num1 * num2

def func_3(num: int) -> str:
    bool = True if num % 2 == 0 else False
    return 'Liczba parzysta' if bool else 'Liczba nieparzysta'

def func_4(num1: int, num2: int, num3: int) -> bool:
    return True if num1*num2 > num3 else False

if __name__ == '__main__':

    func_1('Adam', 'Kowalski')
    func_2(3, 4)
    func_3(6)
    func_4(1, 3, 5)
