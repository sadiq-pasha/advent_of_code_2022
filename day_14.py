from day_14_input import day_14_input as raw_input_data

raw_input_data = [[*map(eval,row.split(" -> "))] for row in raw_input_data.split("\n")]
# print(raw_input_data)
columns,rows = set(),set()
for row in raw_input_data:
    for tile in row:
        columns.add(tile[0])
        rows.add(tile[1])
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

for row in raw_input_data:
    grid[row[0][1]][row[0][0]-column_start] = "#"
    for move_index,move in enumerate(row[1:]):
        if move[0] == row[move_index][0]:
            for _ in range(min(move[1],row[move_index][1]),max(move[1],row[move_index][1])+1):
                grid[_][move[0]-column_start] = "#"
        elif move[1] == row[move_index][1]:
            for _ in range(min(move[0],row[move_index][0]),max(move[0],row[move_index][0])+1):
                grid[move[1]][_-column_start] = "#"

# class particle:
#     def __init__(self) -> None:
#         self.start = [0,500-column_start]
#     def get_position(self):
#         return [self.start[0],self.start[1]]
# grid[9][500-column_start] = "."
out_of_bounds = False
# for last_tile in range(len(grid[-1])):
#     print(grid[-1])
#     grid[-1][last_tile] = '#'
for _ in grid:
    print("".join(_))
def move_down(number,particle,):
    # out of bounds
    global out_of_bounds
    if particle[0]+1 > len(grid) - 1:
        print("out of bounds")
        out_of_bounds = True
        return False
    if grid[particle[0]+1][particle[1]] == "o" or grid[particle[0]+1][particle[1]] == "#":
        # print("no movement down")
        # possible_moves[1] = False
        return False
    while not (particle[0]+1 > len(grid) - 1) and grid[particle[0]+1][particle[1]] == ".":
        print(f"particle {number} moved to {particle}")
        particle[0] += 1
    return True

def move_left(number,particle,):
    # out of bounds
    global out_of_bounds
    if particle[1]-1 < 0 or particle[0]+1 > len(grid)-1:
        # print("out of bounds")
        out_of_bounds = True
        return False
    if grid[particle[0]+1][particle[1]-1] == ".":
        # print(particle,grid[particle[0]+1][particle[1]])
        particle[0] += 1
        particle[1] -= 1
        print(f"particle {number} moved to {particle}")
        return True
    elif grid[particle[0]+1][particle[1]-1] == "o" or grid[particle[0]+1][particle[1]-1] == "#":
        # print("no movement left")
        # possible_moves[0] = False
        return False

def move_right(number,particle,):
    # out of bounds
    global out_of_bounds
    if particle[1]+1 > len(grid[0])-1 or particle[0]+1 > len(grid)-1:
        # print("out of bounds")
        out_of_bounds = True
        return False
    if grid[particle[0]+1][particle[1]+1] == ".":
        # print(particle,grid[particle[0]+1][particle[1]])
        particle[0] += 1
        particle[1] += 1
        print(f"particle {number} moved to {particle}")
        return True
    elif grid[particle[0]+1][particle[1]+1] == "o" or grid[particle[0]+1][particle[1]+1] == "#":
        # print("no movement right")
        # possible_moves[2] = False
        return False

particle_list = []
i = 0
while not out_of_bounds:
    # possible_moves = [True,True,True]
    particle = [0,500-column_start]
    particle_list.append(particle)
    while True:
        if move_down(i,particle_list[-1]):
            # print("moving down")
            if out_of_bounds:
                break
            continue
        elif move_left(i,particle_list[-1]):
            # print("moving left")
            if out_of_bounds:
                break
            continue
        elif move_right(i,particle_list[-1]):
            # print("moving right")
            if out_of_bounds:
                break
            continue
        elif [move_down(i,particle_list[-1]),(move_left(i,particle_list[-1])),(move_right(i,particle_list[-1]))].count(False) == 3:
            # print([move_down(i,particle_list[-1]),(move_left(i,particle_list[-1])),(move_right(i,particle_list[-1]))])
            break
    i += 1
    for particle in particle_list:
        grid[particle[0]][particle[1]] = "o"
    # for _ in grid:
    #     print("".join(_))
    # move_left(i,particle_list[-1])

# print(particle_list)
# for i,j in enumerate(particle_list):
#     grid[j[0]][j[1]] = f"{i}"

if out_of_bounds:
    grid[particle_list[-1][0]][particle_list[-1][1]] = "X"
for _ in grid:
    print("".join(_))
print(len(particle_list))