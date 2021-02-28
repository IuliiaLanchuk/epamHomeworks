import sys
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    maxValue = 0
    minValue = sys.maxsize
    with open(file_name) as fi:
        for line in fi:
            number = int(line.rstrip())
            if number > maxValue:
                maxValue = number
            if number < minValue:
                minValue = number
    return minValue, maxValue


print(find_maximum_and_minimum("some_file.txt"))
