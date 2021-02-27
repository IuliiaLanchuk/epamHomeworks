from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    isFib = len(data) >= 3
    if isFib:
        for i in range(len(data) - 2):
            if (data[i] + data[i + 1]) != data[i + 2]:
                isFib = False
                break
    return isFib


a = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]
# a = []
print("it's a fib sequence!" if check_fibonacci(a) else "Invalid data")
