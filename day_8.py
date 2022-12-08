from day_8_input import day_8_input as raw_input_data

# Create a matrix of trees given input data
# Transpose the matrix, converting colums into rows in order to reuse row logic
tree_matrix = [tuple(tree for tree in row) for row in raw_input_data.split("\n")]
transposed_tree_matrix = list(zip(*tree_matrix))

# Calculate the vision score for each tree
def vision_score(tree_value, neighbours):
    vis_score = 0
    for neighbour in neighbours:
        if neighbour >= tree_value:
            vis_score += 1
            break
        vis_score += 1
    return vis_score

invisible_trees = 0
total_trees = len(tree_matrix) * len(tree_matrix[0])
vision_score_list = []

# For each tree isolate left and right neighbours. Find the max of each side; if max(side) == tree height, tree is invisible from that side
# Repeat process for transposed matrix. In the transpose the left/right neighbours are top/down neighbours from the original matrix
#   this allows us to reuse the same logic. However, the [row][column] indexing must be changed to [column][row] to account for the transpose
for row in range(1 , len(tree_matrix)-1):
    for column in range(1 , len(tree_matrix[0])-1):
        if (tree_matrix[row][column] <= max(tree_matrix[row][:column]) and tree_matrix[row][column] <= max(tree_matrix[row][column+1:])):
            if (transposed_tree_matrix[column][row] <= max(transposed_tree_matrix[column][:row]) and transposed_tree_matrix[column][row] <= max(transposed_tree_matrix[column][row+1:])):
                invisible_trees += 1
        # Calculate vision score for each tree in each cardinal direction
        # Append the vision score to [vision_score_list]
        vision_left = vision_score(tree_matrix[row][column], reversed(tree_matrix[row][:column]))
        vision_right = vision_score(tree_matrix[row][column], tree_matrix[row][column+1:])
        vision_top = vision_score(transposed_tree_matrix[column][row], reversed(transposed_tree_matrix[column][:row]))
        vision_bottom = vision_score(transposed_tree_matrix[column][row] ,transposed_tree_matrix[column][row+1:])
        vision_score_list.append(vision_left * vision_right * vision_top * vision_bottom)
        
# Problem one: 1533
print(f"visible trees: {total_trees-invisible_trees}")
# Problem two: 345744
print(f"higest vision score: {max(vision_score_list)}")