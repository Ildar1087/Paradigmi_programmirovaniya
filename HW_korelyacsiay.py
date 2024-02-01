from functools import reduce
import math


def correlation(data_1, data_2):
    n = len(data_1)  # количество элементов в массиве data_1
    mean_1 = sum(data_1) / n  # среднее значение для data_1
    mean_2 = sum(data_2) / n  # среднее значение для data_2

    deviation_1 = list(map(lambda x: x - mean_1, data_1))  # отклонения
    deviation_2 = list(map(lambda x: x - mean_2, data_2))

    numerator = reduce(lambda x, y: x + y[0] * y[1], zip(deviation_1, deviation_2), 0)

    denominator = \
        math.sqrt(reduce(lambda x, y: x + y ** 2, deviation_1, 0)) \
        * math.sqrt(reduce(lambda x, y: x + y ** 2, deviation_2, 0))
    if denominator == 0:
        return 0
    return numerator / denominator

data_1 = [1,2,3,4,5,6]
data_2 = [3,4,2,4,3,11]
result = correlation(data_1, data_2)
print(result)
