from day_2_input import day_2_input as raw_input_data

# parse the input data
raw_input_data = raw_input_data.split("\n")
# raw_input_data = ["A Y","B X","C Z"]
# dictionary of points for every possible round
case_dict = {"A X": (4,"Z"),
             "A Y": (8,"X"),
             "A Z": (3,"Y"),
             "B X": (1,"X"),
             "B Y": (5,"Y"),
             "B Z": (9,"Z"),
             "C X": (7,"Y"),
             "C Y": (2,"Z"),
             "C Z": (6,"X")}

# obtain each rounds score using the dictionary
# and mapping each round using a lambda
# sum the array to find the score
def score_calculator(input_data):
    return sum(map(lambda x: case_dict[x][0], input_data))

print(score_calculator(raw_input_data))

# change the shapes played based on the new rules
def change_shapes_played(shapes_played):
    return shapes_played[0]+" "+case_dict[shapes_played][1]

new_rules_data = list(map(change_shapes_played, raw_input_data))
print (score_calculator(new_rules_data))


