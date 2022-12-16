from day_14_input import day_14_input as raw_input_data

# REFER TO DAY_14_PART_ONE for detailed comments on code execution. The setup for both problems is identical. Only pertinent changes are commented here

# Parse input data and initialise grid, add two extra rows as per problem statement
raw_input_data = [[*map(eval,row.split(" -> "))] for row in raw_input_data.split("\n")]
columns,rows = set(),set()
for row in raw_input_data:
    for tile in row:
        columns.add(tile[0])
        rows.add(tile[1])
grid = []
row_start = 0
row_end = max(rows) + 2
column_start = min(columns)
column_end =  max(columns)
for row in range(row_start,row_end+1):
    row = []
    for column in range(column_start,column_end+1):
        row.append(".")
    grid.append(row)

# For each line in the input data, draw the cave structure using the rules set out for parsing the input
for row in raw_input_data:
    grid[row[0][1]][row[0][0]-column_start] = "#"
    for move_index,move in enumerate(row[1:]):
        if move[0] == row[move_index][0]:
            for _ in range(min(move[1],row[move_index][1]),max(move[1],row[move_index][1])+1):
                grid[_][move[0]-column_start] = "#"
        elif move[1] == row[move_index][1]:
            for _ in range(min(move[0],row[move_index][0]),max(move[0],row[move_index][0])+1):
                grid[move[1]][_-column_start] = "#"

# for this problem the last row is all rock, change the last row of the grid to reflect that
for last_tile in range(len(grid[-1])):
    grid[-1][last_tile] = '#'

# for _ in grid:
#     print("".join(_))

# The logic for movement is the same as problem one. The difference being that there are no checks for out of bounds conditions
# as there is an infinite floor at the bottom as described in the problem statement
def move_down(particle):
    if particle[0]+1 > len(grid) - 1:
        return False
    # if downward movement blocked, return False
    if grid[particle[0]+1][particle[1]] == "o" or grid[particle[0]+1][particle[1]] == "#":
        return False
    # while downward movement is not blocked, move down
    while not (particle[0]+1 > len(grid) - 1) and grid[particle[0]+1][particle[1]] == ".":
        particle[0] += 1
    return True

# Here the two solutions vary greatly, if a particles next diagonal move takes it out of the grid, create an additional column on the left side.
# This moves the relative position of the "particle spawner" and all previously placed particles.
# Therefore iterate through all the particles and increment their x coordinates by one
# Additionally decrement the x coordinate of the "particle spawner" by one to keep it in the same relative position to the growing grid
def move_left(particle):
    global column_start
    if particle[1]-1 < 0 or particle[0]+1 > len(grid)-1:
        column_start -= 1
        # insert empty column at the start of the grid
        for _ in grid:
            _.insert(0,".")
        # change the last row to rock as per problem statement
        grid[-1][0] = "#"
        # update particle coordinates 
        for particle in particle_list:
            particle[1] += 1
        # call this function again to move the particle into the newly created column
        move_left(particle)
        return
    # move particle diagonally left if possible and return True
    if grid[particle[0]+1][particle[1]-1] == ".":
        particle[0] += 1
        particle[1] -= 1
        return True
    # if movement not possible return False
    elif grid[particle[0]+1][particle[1]-1] == "o" or grid[particle[0]+1][particle[1]-1] == "#":
        return False

def move_right(particle):
    # similar to move_left, if next diagonal right move causes an out of bounds condition, add an empty column to the right whose last element is a rock
    if particle[1]+1 > len(grid[0])-1 or particle[0]+1 > len(grid)-1:
        for _ in grid:
            _.append(".")
        grid[-1][-1] = "#"
        move_right(particle)
        return
    if grid[particle[0]+1][particle[1]+1] == ".":
        particle[0] += 1
        particle[1] += 1
        return True
    elif grid[particle[0]+1][particle[1]+1] == "o" or grid[particle[0]+1][particle[1]+1] == "#":
        return False

particle_list = []
while True:
    # particle spawner
    particle = [0,500-column_start]
    particle_list.append(particle)
    # move the particle in priority order (down,left,right). At every move, return to the top of the loop
    while True:
        if move_down(particle_list[-1]):
            continue
        elif move_left(particle_list[-1]):
            continue
        elif move_right(particle_list[-1]):
            continue
        # if no more moves possible, break
        elif [move_down(particle_list[-1]),(move_left(particle_list[-1])),(move_right(particle_list[-1]))].count(False) == 3:
            break
    # place the particles in the grid
    for particle in particle_list:
        grid[particle[0]][particle[1]] = "o"
    # if the last placed particle, covers the "particle spawner", break
    if particle_list[-1] == [0,500-column_start]:
        break

# draw the final grid
# for _ in grid:
#     print("".join(_))

# write the output to day_14_part_two_output.txt
# with open('day_14_part_two_output.txt', 'w') as f:
#     for _ in grid:
#         f.writelines(_)
#         f.write('\n')

# problem two: consider the grid with an infinite floor, how many particles come to rest before the "particle spawner" is covered
print(len(particle_list))