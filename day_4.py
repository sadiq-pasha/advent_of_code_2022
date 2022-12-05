from day_4_input import day_4_input as raw_input_data

# problem one
# split data by line
split_data = raw_input_data.split("\n")

# split data into pairs
split_data = list(map(lambda pair: pair.split(","), split_data))

# convert each pair into upper and lower limit tuples
for index, line in enumerate(split_data):
    a = map(int,line[0].split("-"))
    b = map(int,line[1].split("-"))
    split_data[index] = [tuple(a),tuple(b)]

# sort each pair based on length, with the longer range first
for pair in split_data:
    pair.sort(key=lambda region: region[1] - region[0],reverse=True)

# if second tuple is contained within the first, increment counter
problem_one_counter = 0
for section_pair in split_data:
    if section_pair[0][0] <= section_pair[1][0] and section_pair[0][1] >= section_pair[1][1]:
        problem_one_counter += 1

print(problem_one_counter)

# problem two
# expand overlap criteria to check if each tuple begins within the other
problem_two_counter = 0
for section_pair in split_data:
    if (
        section_pair[0][0] >=section_pair[1][0] and section_pair[0][0] <=section_pair[1][1]
        ) or (
            section_pair[1][0] >=section_pair[0][0] and section_pair[1][0] <=section_pair[0][1]
            ):
        problem_two_counter += 1

print(problem_two_counter)