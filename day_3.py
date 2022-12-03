from day_3_input import day_3_input as raw_data_input

import itertools

# raw_data_input = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

# part one solution
sum_of_duplicates = sum(map(lambda duplicate: (ord(duplicate)-38) if (ord(duplicate)<96) else (ord(duplicate)-96),itertools.chain.from_iterable(map(lambda knapsack: set(knapsack[:(len(knapsack)//2)]).intersection(set(knapsack[(len(knapsack)//2):])), raw_data_input.split("\n")))))
# print(sum_of_duplicates)