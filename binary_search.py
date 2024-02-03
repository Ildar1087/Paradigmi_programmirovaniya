# Задача: Реализовать бинарный поиск элемента в массиве.
# Решение реализовано с помощью императивной парадигмы, 
# а в частности процедурной и структурной парадигм
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# binary_search([1, 23, 21, 11, 19, 5, 8, 4, 3, 88], 8)
