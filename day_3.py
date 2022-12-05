from day_3_input import day_3_input as raw_data_input
import itertools

# raw_data_input = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

# part one solution
# split raw data into array with individual knapsacks                                raw_data_input.split("\n")
# split each knapsack into equally sized compartments                                knapsack[:(len(knapsack)//2)] , knapsack[(len(knapsack)//2):]
# create a set for each compartment (to eliminate duplicates)                        set(knapsack[:(len(knapsack)//2)]) , set(knapsack[(len(knapsack)//2):])
# find the overlapping elements using set method intersection                        set(knapsack[:(len(knapsack)//2)]).intersection(set(knapsack[(len(knapsack)//2):]))
# combine all sets of overlapping elements into a list using itertools.chain         itertools.chain.from_iterable(set(knapsack[:(len(knapsack)//2)]).intersection(set(knapsack[(len(knapsack)//2):])))
# for each element convert to int using priority list:
#   Lowercase item types a through z have priorities 1 through 26.                   ord(duplicate)-96
#   Uppercase item types A through Z have priorities 27 through 52.                  ord(duplicate)-38) if (ord(duplicate)<96
# find the sum of the ords and print
sum_of_duplicates = sum(map(lambda duplicate: (ord(duplicate)-38) if (ord(duplicate)<96) else (ord(duplicate)-96),itertools.chain.from_iterable(map(lambda knapsack: set(knapsack[:(len(knapsack)//2)]).intersection(set(knapsack[(len(knapsack)//2):])), raw_data_input.split("\n")))))
print(sum_of_duplicates)


# part two solution
# split raw data into knapsacks in an array
array_raw_input = raw_data_input.split("\n")

# group the knapsacks in three's
grouped_knapsacks = []
subgrouped_knapsacks = []
group_counter = 0

for knapsack in array_raw_input:
    subgrouped_knapsacks.append(knapsack)
    group_counter += 1
    if group_counter  == 3:
        grouped_knapsacks.append(subgrouped_knapsacks)
        subgrouped_knapsacks = []
        group_counter = 0

# for each group eliminate duplicates per knapsack
for group in grouped_knapsacks:
    for index, knapsack in enumerate(group):
        group[index] = set(knapsack)

# find the intersection of the knapsacks in each group
# convert to list and store
array_group_duplicates = []
for group in grouped_knapsacks:
    array_group_duplicates.append(list(set.intersection(*group)))

# convert each groups duplicate into its ordinate 
# ord(a) - ord(z)       ord(A) - ord(Z)
#   97       122         65       90            ordinate
#  -96       -96        -38      -38            normalizer
#  = 1       =26        =27      =52            code as defined
# if ord(duplicate) is less than 96, its an uppercase character, subtract 38
# if ord(duplicate) is greater than 96, its lowercase, subtract 96
array_ordinates = []
for group_duplicate in array_group_duplicates:
    for duplicate in group_duplicate:
        if ord(duplicate) < 96:
            array_ordinates.append(ord(duplicate)-38)
        else:
            array_ordinates.append(ord(duplicate)-96)

# sum of duplicate ordinates
print(sum(array_ordinates))