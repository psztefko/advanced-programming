
def task_a(names):
    for name in names:
        print(name)

def task_b1(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

def task_b2(numbers):
    return [number*2 for number in numbers]

def task_c():
    print([element for element in range(10) if element%2 == 0])

def task_d():
    print([element for element in range(10) if int(element)%2 == 0])

if __name__ == '__main__':

    print('task A: ')
    task_a(['Bartek', 'Ania', 'Kuba', 'Kasia', 'Maciek'])
    print('task B1 and B2: ')
    task_b1([3, 2, 1, 5, 7])
    print(task_b2([3, 2, 1, 5, 7]))
    print('task C: ')
    task_c()
    print('task D: ')
    task_d()