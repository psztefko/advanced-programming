
def task_a(names):
    for name in names:
        print(name)

def task_b1(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

def task_b2(numbers):
    return [number*2 for number in numbers]

def task_c(list):
    for i in range(len(list)):
        print(i) if i%2 == 0 else None

if __name__ == '__main__':

    #task_a(['Bartek', 'Ania', 'Kuba', 'Kasia', 'Maciek'])
    #task_b1([3, 2, 1, 5, 7])
    #print(task_b2([3, 2, 1, 5, 7]))
    task_c([element for element in range(10)])
