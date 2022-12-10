from day_10_input import day_10_input as raw_input_data
raw_data = raw_input_data.split("\n")

# __init__
register = 1
cycle_counter = 0
message = []

# create crt screen
crt_screen_size = 240
crt = ["." for _ in range(crt_screen_size)]

# check cycle counter and update message for problem one and crt for problem two
def signal_check(register, cycle_counter):
    check_times = [20,60,100,140,180,220]
    global crt
    global message
    sprite = [register-1, register, register+1]
    if cycle_counter % 40 in sprite:
        crt[cycle_counter] = "#"
    if cycle_counter in check_times:
        message.append((cycle_counter, cycle_counter * register))

# for problem one move signal check below cycle pointer increment
def noop(register, cycle_counter):
    signal_check(register, cycle_counter)
    cycle_counter += 1
    return register, cycle_counter

# for problem one move signal check below cycle pointer increment
def add(register, cycle_counter, value):
    signal_check(register, cycle_counter)
    cycle_counter += 1
    signal_check(register, cycle_counter)
    cycle_counter +=1
    register += value
    return register, cycle_counter

for instruction in raw_data:
    if instruction == "noop":
        register, cycle_counter = noop(register, cycle_counter)
    elif instruction[:4] == "addx":
        value = int(instruction.split(" ")[1])
        register, cycle_counter = add(register, cycle_counter, value)

print(sum([_[1] for _ in message]))

def print_crt(crt):
    width = 40
    for i in range(0,len(crt),width):
        print(crt[i:i+width])
print_crt("".join(crt))