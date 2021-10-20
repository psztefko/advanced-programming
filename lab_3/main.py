

def func_1(name: str, surname: str) -> str:
    return f'Cześć {name} {surname}!'

def func_2(num1: int, num2: int) -> int:
    return num1 * num2


if __name__ == '__main__':

    func_1('Adam', 'Kowalski')
    func_2(3, 4)