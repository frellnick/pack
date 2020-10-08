# gen_test.py

"""
Generate Tests

Build single table and linked table tests for pack group.
"""
from itertools import combinations


def _gen_combinations(filenames:list)->list:
    return list(combinations(filenames, 2))


def gen_test(filenames:list):
    combinations = _gen_combinations(filenames)
    print(combinations)



if __name__ == "__main__":
    tfiles = ['f1.csv', 'f2.csv', 'f3.csv']
    gen_test(tfiles)