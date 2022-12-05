from day_5_input import crate_info as crate_info
from day_5_input import move_list as move_list

raw_data = crate_info.split("\n")

# find indices of the stacks in the raw data file
stack_indices = []
for index,stack_numbers in enumerate(raw_data[-1]):
    if stack_numbers != " ":
        stack_indices.append((stack_numbers, index))

# using [stack indices], pull the crates from the raw data file
# and populate into [stack array]
stack_array = []
for i, stack_index in enumerate(stack_indices):
    index = stack_index[1]
    stack = []
    for data_row in raw_data[:-1]:
        if data_row[index] != " ":
            stack.append(data_row[index])
    stack_array.append(stack)
# flip the arrays for easier pop and push
for stack in stack_array:
    stack.reverse()

# extract crate move information
crate_moves = []
for row in [_.split(" ") for _ in move_list.split("\n")]:
    crate_moves.append(tuple([*map(int,filter(lambda word: word.isnumeric(), row))]))

# problem one
# move [times] number of crates from [origin] to [destination]
for times, origin, destination in crate_moves:
    for time in range(times):
        temp = stack_array[origin-1].pop()
        stack_array[destination-1].append(temp)

# return a string with the top crates from each stack
top_crates = "".join([_[-1] for _ in stack_array])
print(top_crates)

# problem two
# move [times] number of crates from [origin] to [destination]
for move_size, origin, destination in crate_moves:
        temp = stack_array[origin-1][-move_size:]
        stack_array[origin-1] = stack_array[origin-1][:len(stack_array[origin-1])-move_size]
        stack_array[destination-1].extend(temp)

top_crates = "".join([_[-1] for _ in stack_array])
print(top_crates)