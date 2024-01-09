### задача №1
### Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для сортировки числа в
### порядке убывания. Можно использовать любой алгоритм сортировки.
###
from random import randint
from typing import List


def sort_list_imperative(numbers: List[int]) -> List[int]:
    """Используем метод сортировки пузырьком. Попарно сравнивая соседние элементы и меняя местами,
    если правый элемент больше левого. Процесс проходит в несколько итераций"""
    if len(numbers) == 0:
        raise ValueError('На вход подаётся непустой целочисленный список!!!')
    for i in range(0, len(numbers)-1):
        for j in range(len(numbers) -1):
            if (numbers[j] < numbers[j+1]):
                numbers[j], numbers [j+1] = numbers[j+1], numbers[j]
    return numbers

numbers = [randint(0, 10) for i in range(9)]
print(numbers)
print(sort_list_imperative(numbers))
print("================================")


### задача №2
### Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру для сортировки числа в
### порядке убывания. Можно использовать любой алгоритм сортировки.
###
def sort_list_declarative(numbersD: List[int])-> List[int]:
    if len(numbersD) == 0:
        raise ValueError('На вход подается непустой целочисленный список!!!')
    '''Воспользуемся встроенным методом sorted из библиотеки python и развернём список с 
    помощью reverse в порядке убывания'''
    return sorted(numbersD, reverse=True)

numbersD = [randint(0, 11) for i in range(9)]
print(numbersD)
print(sort_list_declarative(numbersD))
