from day_15_input import day_15_input as raw_input_data
import re
from collections import defaultdict

# find all integer coordinates in the input and create a coordinate list [(sensor_x,sensor_y),(beacon_x,beacon_y)]
coordinates_list = []
for row in raw_input_data.split("\n"):
    x1,y1,x2,y2 = re.findall('[-+]?\d+', row)
    coordinates_list.append([[eval(x1),eval(y1)],[eval(x2),eval(y2)]])

# function to calculate the manhattan distance between two points
def manhattan_distance(sensor_beacon_pair):
    sensor,beacon = sensor_beacon_pair
    return abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

# code block to calculate the min/max x/y coordinates for the grid
# initially find the min/max for each set of sensor coordinates
min_x_coord = min(pair[0][0] for pair in coordinates_list)
max_x_coord = max(pair[0][0] for pair in coordinates_list)
min_y_coord = min(pair[0][1] for pair in coordinates_list)
max_y_coord = max(pair[0][1] for pair in coordinates_list)
# further add the manhattan distance between the sensor and the beacon to the min/max coordinates
# this allows us to draw the grid without any out of bounds conditions
# for example: initially the min/max calculation puts the min_y_coord at the location of the the beacon B at (0,0)
# but when the manhattan distance is drawn; the far left of the diamond will be out of bounds. 
# we need to find the min_y_coord including the manhattan diamonds. coordinates of the becon B are now (0,4)
#   BEFORE: B....       AFTER:  ...B####
#           .....               ..######
#           .....               .#######
#           ....S               #######S

for sensor_beacon_pair in coordinates_list:
    distance = manhattan_distance(sensor_beacon_pair)
    if sensor_beacon_pair[0][0] - distance < min_x_coord:
        min_x_coord = sensor_beacon_pair[0][0] - distance
    if sensor_beacon_pair[0][0] + distance > max_x_coord:
        max_x_coord = sensor_beacon_pair[0][0] + distance
    if sensor_beacon_pair[0][1] - distance < min_y_coord:
        min_y_coord = sensor_beacon_pair[0][1] - distance
    if sensor_beacon_pair[0][1] + distance > max_y_coord:
        max_y_coord = sensor_beacon_pair[0][0] + distance
# now that new min/max coords have been calculated, we need to shift all the points to the right 
# in order to make room for the diamonds. add min_x_coord to x coordinates and min_y_coord to y coordinates
for pair in coordinates_list:
    pair[0][0] += abs(min_x_coord)
    pair[0][1] += abs(min_y_coord)
    pair[1][0] += abs(min_x_coord)
    pair[1][1] += abs(min_y_coord)

# this code block draws the grid, uncomment for small grids. 
# creating a grid for LARGE values of x/y causes a memory error
# grid = []
# for i in range(min_x_coord-1,max_x_coord+1):
#     row = []
#     for j in range(min_y_coord-1, max_y_coord+1):
#         row.append(".")
#     grid.append(row)

# function that solves problem one
# given a line of interest. In this case it is 10. we first find all the becons located on this line
def problem_one(line_of_interest):
    # normalize the line of interest to our new minimum y coordinate
    line_of_interest += abs(min_y_coord)
    # for all beacon coordinates, find any that have y coordinate on the line of interest
    # multiple sensors can have the same beacon so avoid duplicates
    beacons_on_line_of_interest = []
    for pair in coordinates_list:
        if pair[1][1] == line_of_interest and pair[1] not in beacons_on_line_of_interest:
            beacons_on_line_of_interest.append(pair[1])
    
    # find the area covered by any sensor that projects over the line of interest 
    line_of_interest_sensor_coverage = []
    for pair in coordinates_list:
        start = pair[0][0]-manhattan_distance(pair)
        end = pair[0][0]+manhattan_distance(pair)
        vertical_delta = 0
        # for each sensor in the list, find its area of coverage. 
        # if the area of coverage crosses the line of interest: append that area to line_of_interest_sensor_coverage
        while start <= end:
            if pair[0][1]-vertical_delta == line_of_interest:
                line_of_interest_sensor_coverage.append([start,end])
            elif pair[0][1]+vertical_delta == line_of_interest:
                line_of_interest_sensor_coverage.append([start,end])
            # uncomment this if grid is drawn for small input data sets
            # for i in range(start,end+1):
            #     grid[pair[0][1]-vertical_delta][i] = "#"
            #     grid[pair[0][1]-vertical_delta][i] = "#"
            #     grid[pair[0][1]+vertical_delta][i] = "#"
            #     grid[pair[0][1]+vertical_delta][i] = "#"          
            start += 1
            end -= 1
            vertical_delta += 1
    # uncomment this if grid is drawn for small input data sets
    # for pair in coordinates_list:
    #     grid[pair[0][1]][pair[0][0]] = "S"
    #     grid[pair[1][1]][pair[1][0]] = "B"
    # for _ in grid:
    #     print("".join(_))

    # sort the areas covered by sensors on the line and collapse intersecting areas
    line_of_interest_sensor_coverage.sort()    
    unique_sensor_coverage = [line_of_interest_sensor_coverage[0]]
    for sensor_coverage in sorted(line_of_interest_sensor_coverage)[1:]:
        if sensor_coverage[0] > unique_sensor_coverage[-1][1]:
            unique_sensor_coverage.append(sensor_coverage)
        elif sensor_coverage[0] <= unique_sensor_coverage[-1][1]:
            unique_sensor_coverage[-1][1] = max(sensor_coverage[1],unique_sensor_coverage[-1][1])
    
    impossible_sensor_positions = 0
    # for each area of sensor coverage [start,end] add the number of tiles (end-start) to impossible_sensor_positions
    for unique_sensors in unique_sensor_coverage:
        impossible_sensor_positions += (unique_sensors[1] - unique_sensors[0] + 1)
    # return value of all impossible locations after removing the number of beacons on the line as found in beacons_on_line_of_interest
    print(impossible_sensor_positions - len(beacons_on_line_of_interest))

problem_one(10)

# memoisation for problem two. This drastically reduces compute time as the coverage of each sensor doesnt need to be recalculated
# create a dictionary of all lines covered by all sensors
# line_of_interest_sensor_coverage = {line_number: [start_of_coverage,end_of_coverage]}
line_of_interest_sensor_coverage = defaultdict(lambda:[])
def sensor_coverage_finder():
    for pair in coordinates_list:
        start = pair[0][0]-manhattan_distance(pair)
        end = pair[0][0]+manhattan_distance(pair)
        vertical_delta = 0
        while start <= end:
            line_of_interest_sensor_coverage[pair[0][1]-vertical_delta].append([start,end])
            line_of_interest_sensor_coverage[pair[0][1]+vertical_delta].append([start,end])
            start += 1
            end -= 1
            vertical_delta += 1
sensor_coverage_finder()

# function that solves problem two, in between two lines find the only tile where no sensor has coverage
def uncovered_beacon_finder(start_line,end_line):
    # normalize input start and end constraints to the calculated minimum y coordinates of the grid
    line_of_interest_start = start_line + abs(min_y_coord)
    line_of_interest_end = end_line + abs(min_y_coord)
    
    # list of all lines within the search area problem_two_lines 
    # [line number,areas of coverage from the dictionary {line_of_interest_sensor_coverage}]
    problem_two_lines = []
    for line in range(line_of_interest_start,line_of_interest_end+1):
        if line in line_of_interest_sensor_coverage:
            problem_two_lines.append([line,line_of_interest_sensor_coverage[line]])
    
    # for all lines in the search area, sort the areas of coverage and collapse intersecting areas
    problem_two_lines.sort(key=lambda x: x[0])
    for each_line in problem_two_lines:
        sensor_coverage = sorted(each_line[1])
        unique_sensor_coverage = [sensor_coverage[0]]
        for sensor in sensor_coverage[1:]:
            if sensor[0] > unique_sensor_coverage[-1][1]+1:
                unique_sensor_coverage.append(sensor)
            elif sensor[0] <= unique_sensor_coverage[-1][1]+1:
                unique_sensor_coverage[-1][1] = max(sensor[1],unique_sensor_coverage[-1][1])
        each_line[1]= unique_sensor_coverage
        # if there are two areas after collapse, it means there is a gap between the areas of coverage
        # this is the uncovered beacon
        # find the x,y coordinates; denormalize them and return
        if len(each_line[1]) > 1:
            x = (each_line[1][0][1] + 1) -abs(min_x_coord)
            y = each_line[0]-abs(min_y_coord)
            print((x*4000000)+y)
            break
uncovered_beacon_finder(0,20)