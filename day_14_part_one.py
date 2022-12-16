from day_14_input import day_14_input as raw_input_data

# split input data into rows and convert to list using eval
raw_input_data = [[*map(eval,row.split(" -> "))] for row in raw_input_data.split("\n")]

# create set of all x and y coordinates to find the grid boundaries
columns,rows = set(),set()
for row in raw_input_data:
    for tile in row:
        columns.add(tile[0])
        rows.add(tile[1])
# initialise the grid using min/max of rows and columns. Row start is 0 because the sand falls from [0,500]
grid = []
row_start = 0
row_end = max(rows)
column_start = min(columns)
column_end =  max(columns)
for row in range(row_start,row_end+1):
    row = []
    for column in range(column_start,column_end+1):
        row.append(".")
    grid.append(row)

# using the rules for parsing input data into the cave system, create the cave system.
for row in raw_input_data:
    # place the first rock at the start of each input line
    grid[row[0][1]][row[0][0]-column_start] = "#"
    for move_index,move in enumerate(row[1:]):
        # if the x coordinates are equal move in the y direction
        if move[0] == row[move_index][0]:
            for _ in range(min(move[1],row[move_index][1]),max(move[1],row[move_index][1])+1):
                # place rocks at all y coordinates in between the two inputs
                grid[_][move[0]-column_start] = "#"
        # if the y coordinates are equal move in the x direction
        elif move[1] == row[move_index][1]:
            # place rocks between the the two inputs
            for _ in range(min(move[0],row[move_index][0]),max(move[0],row[move_index][0])+1):
                grid[move[1]][_-column_start] = "#"

# create an out of bounds variable
out_of_bounds = False

# for _ in grid:
#     print("".join(_))

# function to move the sand particle down one tile
def move_down(particle,):
    global out_of_bounds
    # if next move down causes an out of bounds condition, set out_of_bounds and return False
    if particle[0]+1 > len(grid) - 1:
        print("out of bounds")
        out_of_bounds = True
        return False
    # if move down is blocked return False
    if grid[particle[0]+1][particle[1]] == "o" or grid[particle[0]+1][particle[1]] == "#":
        return False
    # while no rocks or sand, move particle down 
    while not (particle[0]+1 > len(grid) - 1) and grid[particle[0]+1][particle[1]] == ".":
        particle[0] += 1
    return True

# function to move the sand particle diagonally left one tile
def move_left(particle,):
    global out_of_bounds
    # if next move diagonally left is out of bounds, set out_of_bounds and return False
    if particle[1]-1 < 0 or particle[0]+1 > len(grid)-1:
        out_of_bounds = True
        return False
    # if diagonally left is open, move particle to that position
    if grid[particle[0]+1][particle[1]-1] == ".":
        particle[0] += 1
        particle[1] -= 1
        return True
    # if diagonally left is blocked, return False
    elif grid[particle[0]+1][particle[1]-1] == "o" or grid[particle[0]+1][particle[1]-1] == "#":
        return False
# function to move the sand particle diagonally right one tile
def move_right(particle,):
    global out_of_bounds
    # if next move diagonally right is out of bounds, set out_of_bounds and return False
    if particle[1]+1 > len(grid[0])-1 or particle[0]+1 > len(grid)-1:
        out_of_bounds = True
        return False
    # if diagonally right is open, move diagonally right one tile
    if grid[particle[0]+1][particle[1]+1] == ".":
        particle[0] += 1
        particle[1] += 1
        return True
    # if diagonally right is blocked by sand or rock, return False
    elif grid[particle[0]+1][particle[1]+1] == "o" or grid[particle[0]+1][particle[1]+1] == "#":
        return False

# create a particle list to hold x,y coordinates of all particles and draw them on the grid
particle_list = []
while not out_of_bounds:
    # start particle at [0,500]
    particle = [0,500-column_start]
    particle_list.append(particle)
    # First try to move the particle down one tile,
    # if move_down returns False(the path down is blocked) try to move the particle diagonally left one tile. 
    # if move_left returns False, try to move the particle diagonally right one tile.
    # if move_right returns False as well the particle can no longer move anywhere and has come to rest

    # IF AT ANY POINT THE move_left OR move_right FUNCTION RETURNS TRUE AND MOVES THE PARTICLE, EXECUTION IS SENT BACK TO THE START OF THE WHILE LOOP
    # THIS MAKES SURE THAT EVERY TIME THE PARTICLE MOVES IT TRIES TO MOVE IN THE PRIORITY ORDER (down,left,right) AFTER *EACH* STEP

    while True:
        if move_down(particle_list[-1]):
            if out_of_bounds:
                break
            continue
        elif move_left(particle_list[-1]):
            if out_of_bounds:
                break
            continue
        elif move_right(particle_list[-1]):
            if out_of_bounds:
                break
            continue
        # if all three functions return False, the particle has come to rest
        elif [move_down(particle_list[-1]),(move_left(particle_list[-1])),(move_right(particle_list[-1]))].count(False) == 3:
            break
    # based on the new values of the particle after moving, draw the particles on the grid
    for particle in particle_list:
        grid[particle[0]][particle[1]] = "o"

# mark the particle the went out of bounds with an "X"
if out_of_bounds:
    grid[particle_list[-1][0]][particle_list[-1][1]] = "X"

# draw the final grid
# for _ in grid:
#     print("".join(_))

# send the data to the text file day_14_part_one_output.txt
# with open('day_14_part_one_output.txt', 'w') as f:
#     for _ in grid:
#         f.writelines(_)
#         f.write('\n')

# problem one: return the number of particles that come to rest before a particle goes out of bounds
print(len(particle_list)-1)