from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    lst = list(product(a, b, c, d))
    counter = 0

    for i in lst:
        if sum(i[0:4]) == 0:
            counter += 1
            # print(i)
    return counter


a = [1, -2, 3, 4, -5]
b = [6, 7, 2, 9, 5]
c = [-10, 12, -13, 14, 15]
d = [16, 17, 13, 19, 20]
print(check_sum_of_four(a, b, c, d))  # returns 4

# (-2, 2, -13, 13)
# (-5, 2, -10, 13)
# (-5, 2, -13, 16)
# (-5, 5, -13, 13)
