from day_12_input import day_12_input as raw_input_data

# Using input data create a 2D matrix maze
maze = [[elevation for elevation in row] for row in raw_input_data.split("\n")]

# set problem_two_flag = True for problem two (min path from all starting positions "a")
# set problem_two_flag = False for problem one (start at maze postion "S")
problem_two_flag = True

# for problem 2 we have to start at all positions "a", [start] is a list of all positions "a" in the matrix
start = []

# iterate through all elements of the maze, if solving problem one:
    # append start at index (i,j) of position "S" and change "S" to "a" as that is the starting elevation
# if solving problem two:
    # append all occurences of "a" to start list
# set end = (i,j) of position "E"
    # change "E" to "z" as that is the final elevation
for i,row in enumerate(maze):
    for j,step in enumerate(row):
        if maze[i][j] == "S":
            maze[i][j] = "a"
            if not problem_two_flag:
                start.append((i,j))
        if (maze[i][j] == "a") and problem_two_flag:
            start.append((i,j))
        if maze[i][j] == "E":
            end = (i,j)
maze[end[0]][end[1]] = 'z'
# print(f"start: {start} end: {maze[end[0]][end[1]]} at {end}")

# find value of neighbours in 4 cardinal directions. If out of bounds, set value to "x"
def neighbours(i,j,maze):
    neighbours_values=[]
    neighbours_values.append((i-1,j) if i>0 else 'x')
    neighbours_values.append((i,j+1) if j<len(maze[0])-1 else 'x')
    neighbours_values.append((i+1,j) if i<len(maze)-1 else 'x')
    neighbours_values.append((i,j-1) if j>0 else 'x')
    return neighbours_values

# depth first search that returns a dictionary of {child: parent} when path is found, else return False
# three conditions for movement are:
    # 1. current block elevation == next block elevation
    # 2. next block elevation is one higher than current block elevation
    # 3. next block elevation is lower than current block elevation 
def path_search(maze, start):
    parent = {}
    finish = end
    queue = [start]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)
        for node in neighbours(vertex[0],vertex[1],maze):
            if node != 'x':
                if (
                    ord(maze[node[0]][node[1]]) == ord(maze[vertex[0]][vertex[1]]) + 1
                    ) or (
                        ord(maze[node[0]][node[1]]) == ord(maze[vertex[0]][vertex[1]])
                        ) or (
                            ord(maze[node[0]][node[1]]) < ord(maze[vertex[0]][vertex[1]])
                        ):
                    if node == finish:
                        parent[node] = vertex
                        return parent
                    elif node not in visited:
                        parent[node] = vertex
                        visited.add(node)
                        queue.append(node)
    # print("no path found")
    return False

# step counter for path
# if a path is found, we have a path dictionary {parent} that has information on how we got to each node
# using the information we can back track from the end node to the start and count how many steps it took
def steps(parent,start):
    # find the end node in the path dict
    if (end[0],end[1]) in parent.keys():
        count = 1
        to_origin = 0
        # set the step back to the parent of the end node in path dict
        step_back = parent[(end[0],end[1])]
        # while we have not reached the start node, change step back to its parent and increment step pointer
        while to_origin != start:
            to_origin = parent[step_back]
            step_back = to_origin
            count += 1
        return(count)
    else:
        print(f"no path found for {start}")

# for each start position find a path, if path exists find the steps taken by that path and add to steps_list
# return min of steps_list. Remember for problem one len(start) = 1, for problem two len(start) = number of "a" positions in the input
steps_list = []
for start_index in start:
    parent = path_search(maze, start_index)
# if path exists find number of steps taken
    if parent:
        steps_list.append(steps(parent, start_index))
print(min(steps_list))