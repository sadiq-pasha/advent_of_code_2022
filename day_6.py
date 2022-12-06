from day_6_input import day_6_input as raw_data_input
from collections import Counter

# sliding window approach
# for each window create a counter
# output index + window_length if number of unique entries in counter equals window length
def first_unique_character_string(string_length):
    for index in range(len(raw_data_input[:-(string_length-1)])):
        counter = Counter(raw_data_input[index:index+string_length])
        if (len(counter.keys()) == string_length):
            print(index + string_length)
            break

# problem one
first_unique_character_string(4)

# problem two
first_unique_character_string(14)