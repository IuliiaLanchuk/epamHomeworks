# epamHomeworks

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