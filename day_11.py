# hard coded input data
monkey_dict = {
    0: {
        "items": [66, 71, 94],
        "operation": "worry_level * 5",
        "test": "worry_level % 3 == 0",
        "true": 7,
        "false": 4,
        "items_inspected": 0
    },
    1: {
        "items": [70],
        "operation": "worry_level + 6",
        "test": "worry_level % 17 == 0",
        "true": 3,
        "false": 0,
        "items_inspected": 0
    },
    2: {
        "items": [62, 68, 56, 65, 94, 78],
        "operation": "worry_level + 5",
        "test": "worry_level % 2 == 0",
        "true": 3,
        "false": 1,
        "items_inspected": 0
    },
    3: {
        "items": [89, 94, 94, 67],
        "operation": "worry_level + 2",
        "test": "worry_level % 19 == 0",
        "true": 7,
        "false": 0,
        "items_inspected": 0
    },
    4: {
        "items": [71, 61, 73, 65, 98, 98, 63],
        "operation": "worry_level * 7",
        "test": "worry_level % 11 == 0",
        "true": 5,
        "false": 6,
        "items_inspected": 0
    },
    5: {
        "items": [55, 62, 68, 61, 60],
        "operation": "worry_level + 7",
        "test": "worry_level % 5 == 0",
        "true": 2,
        "false": 1,
        "items_inspected": 0
    },
    6: {
        "items": [93, 91, 69, 64, 72, 89, 50, 71],
        "operation": "worry_level + 1",
        "test": "worry_level % 13 == 0",
        "true": 5,
        "false": 2,
        "items_inspected": 0
    },
    7: {
        "items": [76, 50],
        "operation": "worry_level * worry_level",
        "test": "worry_level % 7 == 0",
        "true": 4,
        "false": 6,
        "items_inspected": 0
    }
}
# lowest common multiple of all the monkeys tests
# modulo the worry level with this number to keep 
# the worry number from growing exponentially
lcm = 7*13*5*11*19*2*17*3

# set constants for problem one
iterations = 20
problem_two_flag = False

# change number of iterations for problem two
# also remove the worry level dision
if problem_two_flag:
    iterations = 10000

for round in range(iterations):
    for monkey in monkey_dict:
        # for each monkey in the game follow the rules for each item and move accordingly
        items_to_remove = [] # item index to remove
        for item_index, item in enumerate(monkey_dict[monkey]["items"]):
            # keep track of items inspected
            monkey_dict[monkey]["items_inspected"] += 1
            worry_level = item
            # modulo with the LCM to prevent exponential growth
            worry_level = worry_level % lcm
            worry_level = eval(monkey_dict[monkey]["operation"])
            # if problem one divide worry level by 3
            if not problem_two_flag:
                worry_level = worry_level // 3
            # depending on "truth test" move the items to the corresponding monkey
            if eval(monkey_dict[monkey]["test"]):
                monkey_dict[monkey_dict[monkey]["true"]]["items"].append(worry_level)
                items_to_remove.append(item_index)
            else:
                monkey_dict[monkey_dict[monkey]["false"]]["items"].append(worry_level)
                items_to_remove.append(item_index)
        # if items are thrown to a different monkey, remove that item from current monkeys possession
        new_items = [item for index,item in enumerate(monkey_dict[monkey]["items"]) if index not in items_to_remove]
        monkey_dict[monkey]["items"] = new_items

# list of how many items each monkey handled
monkey_business = []
for monkey in monkey_dict:
    monkey_business.append(monkey_dict[monkey]["items_inspected"])

# print product of top two item handling monkeys as "monkey business"
monkey_business.sort()
print(f"{monkey_business[-1]} * {monkey_business[-2]} = {monkey_business[-1]*monkey_business[-2]}")