# epamHomeworks

**HOMEWORK 1**

**task01**


1. please create your own git repository on github.
2. setup pre-commit hook with `black` and `isort` formatting for the repo
3. initialize .gitignore in the repository root 
4. create a `homework1` directory in the repo
5. then copy the `sample_project` into the directory.
6. fix all bugs in the `sample_project` code
7. write an extra test for each found bug
---

**task02**

Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""

from collections import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:

---

**task03**

Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""

from typing import Tuple

def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:

---

**task04**

Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 в‰¤ N в‰¤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:

---

**task05**

Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
    
"""

from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
