from day_7_input import day_7_input as raw_input_data

raw_data = raw_input_data.split("\n")

# create a tree with each file/subdirectory being a node
class Node:
    # initialise node using node value and calling node as parent
    def __init__(self, node, parent) -> None:
        self.name = node
        self.children = []
        self.parent = parent

    def __repr__(self) -> str:
        return self.name

    # critical function that calculates the size of each node including subdirectories
    def size(self):
        self.size = 0
        for child in self.children:
            # if subdirectory found, calculate size using recursion
            if child.name[:3] == "dir":
                self.size += child.size()
            # else add file size
            else:
                self.size += int(child.name.split(" ")[0])
        dir_sizes.append(self.size)
        print(f"directory: {self.name}, size: {self.size}")
        return self.size
    # create node using calling node as parent and append to [children]
    def add_node(self, child_node, parent_node):
        self.children.append(Node(child_node, parent_node))

# list of all directory sizes
dir_sizes = []

# returns a list of nodes to create for each directory
# by parsing the input file after "$ ls" till the next "$" prefixed command
def isolate_nodes_for_creation(index):
    nodes_to_create = []
    while index < len(raw_data) and raw_data[index][0] != "$":
        nodes_to_create.append(raw_data[index])
        index += 1
    return nodes_to_create

# input parser
for index,command in enumerate(raw_data):
    # create root directory
    if command == "$ cd /":
        root_directory = Node("/", None)
        node_pointer = root_directory
    # create nodes using file/directory names given after "$ ls"
    elif command == "$ ls":
        create_node_list = isolate_nodes_for_creation(index + 1)
        for nodes in  create_node_list:
            node_pointer.add_node(nodes, node_pointer)
    # point to parent directory
    elif command == "$ cd ..":
        node_pointer = node_pointer.parent
    # find child directory and point to it
    elif command[:4] == "$ cd":
        for child in node_pointer.children:
            if child.name == "dir " + command.split()[2]:
                node_pointer = child

# point back to root directory and calculate sizes of all subdirectories
node_pointer = root_directory
node_pointer.size()

# problem one
# return sum of all directories with size <= 100000
print(f"problem one: {sum([_ for _ in dir_sizes if _ <= 100000])}")

# problem two
# find min sized directory to delete in order to meet required_space criteria
total_system_size = 70000000
required_space = 30000000
consumed_space = total_system_size - node_pointer.size  # total system size - root directory size
min_delete_required = required_space- consumed_space
print(f"problem two: {min([_ for _ in dir_sizes if _ >= min_delete_required])}")