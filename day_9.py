from day_9_input import day_9_input as raw_input_data

raw_data = [_.split(" ") for _ in raw_input_data.split("\n")]

# problem one __init__
head_pointer = [0,0]
tail_pointer = [0,0]
unique_tailpointer_visits = []

# problem two __init__
# set rope to True if multiple nodes are to be tracked, else False
rope = False
rope_array = [[0,0] for num_of_ropes in range(10)]
unique_last_pointer_visits = []

# function calculates the delta between the head and tail
# the tails movement is then calculated by looking up the delta in delta_dir
# if rope variable is set, the unique_last_pointer_visits array is updated
# else the unique_tailpointer_visits array is updated
def move_tail(head,tail):
    # directory of tail movements based on delta values
    delta_dir = {
        # north
        (0,2): (0,1),
        # north north west
        (-1,2): (-1,1),
        # west north west
        (-2,1): (-1,1),
        # west
        (-2,0): (-1,0),
        # west south west
        (-2,-1): (-1,-1),
        # south south west
        (-1,-2): (-1,-1),
        # south
        (0,-2): (0,-1),
        # south south east
        (1,-2): (1,-1),
        # east south east
        (2,-1): (1,-1),
        # east
        (2,0): (1,0),
        # east north east
        (2,1): (1,1),
        # north north east
        (1,2): (1,1),
        # diagonal north east
        (2,2): (1,1),
        # diagonal south east
        (2,-2): (1,-1),
        # diagonal south west
        (-2,-2): (-1,-1),
        #diagonal north west
        (-2,2): (-1,1)
    }
    # if delta is large enough, move tail based on the lookup
    if (head[0]-tail[0] , head[1]-tail[1]) in delta_dir:
        delta = delta_dir[(head[0]-tail[0] , head[1]-tail[1])]
        tail[0] = tail[0] + delta[0]
        tail[1] = tail[1] + delta[1]
    if rope:
        if rope_array[-1] not in unique_last_pointer_visits:
            unique_last_pointer_visits.append(rope_array[-1][:])
    else:
        if tail not in unique_tailpointer_visits:
            unique_tailpointer_visits.append(tail[:])

# for each input command, move head in given direction and update the tail
# if rope is True, iterate over the rope list and call move_tail() for each rope using the previous rope as head
# if rope is False, call move_tail() on the single tail pointer
for direction,steps in raw_data:
    if direction == "R":
        for step in range(int(steps)):
            head_pointer[0] += 1
            if rope:
                rope_array[0] = head_pointer
                for rope_index in range(1,len(rope_array[1:])+1):
                    move_tail(rope_array[rope_index-1], rope_array[rope_index])
            else:
                move_tail(head_pointer,tail_pointer)
    elif direction == "L":
        for step in range(int(steps)):
            head_pointer[0] -= 1
            if rope:
                rope_array[0] = head_pointer
                for rope_index in range(1,len(rope_array[1:])+1):
                    move_tail(rope_array[rope_index-1], rope_array[rope_index])
            else:
                move_tail(head_pointer,tail_pointer)
    elif direction == "U":
        for step in range(int(steps)):
            head_pointer[1] += 1
            if rope:
                rope_array[0] = head_pointer
                for rope_index in range(1,len(rope_array[1:])+1):
                    move_tail(rope_array[rope_index-1], rope_array[rope_index])
            else:
                move_tail(head_pointer,tail_pointer)
    elif direction == "D":
        for step in range(int(steps)):
            head_pointer[1] -= 1
            if rope:
                rope_array[0] = head_pointer
                for rope_index in range(1,len(rope_array[1:])+1):
                    move_tail(rope_array[rope_index-1], rope_array[rope_index])
            else:
                move_tail(head_pointer,tail_pointer)

# problem one. rope = False
print(len(unique_tailpointer_visits))
# problem two. rope = True
print(len(unique_last_pointer_visits))