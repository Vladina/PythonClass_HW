from typing import Optional
from random import randint
import numpy as np


class MyMatrix:

    def __init__(self, n:int = 5, m:int = 5, a:int = 0, b:int =0, data: Optional[list] = None):
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self.data = data if data else self.__generate_matrix()

    def __generate_matrix(self):
        return [
            [
                randint(self.a, self.b) for _ in range(self.n)] for _ in range(self.m)
        ]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def max_element(self):
        max_element = max(map(max, self.data))
        return max_element

    def min_element(self):
        min_element = min(map(min, self.data))
        return min_element

    def sum_elements(self):
        return np.sum(self.data)

if __name__ == '__main__':
    from copy import deepcopy
    from copy import copy



matrix1 = MyMatrix(a=1, b=10)
matrix2 = deepcopy(matrix1)

matrix1.data[0][2] = 123

print(matrix2)
print(matrix2.max_element())
print(matrix2.min_element())
print(matrix2.sum_elements())


