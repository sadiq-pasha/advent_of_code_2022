from day_7_input import day_7_input as raw_input_data

raw_data = raw_input_data.split("\n")

class Node:
    def __init__(self, node, parent) -> None:
        self.name = node
        self.children = []
        self.parent = parent

    def __repr__(self) -> str:
        return self.name

    def size(self):
        self.size = 0
        for child in self.children:
            if child.name[:3] == "dir":
                self.size += child.size()
            else:
                self.size += int(child.name.split(" ")[0])
        dir_sizes.append(self.size)
        print(f"directory: {self.name}, size: {self.size}")
        return self.size

    def add_node(self, child_node, parent_node):
        self.children.append(Node(child_node, parent_node))

dir_sizes = []

def isolate_nodes_for_creation(index):
    nodes_to_create = []
    while index < len(raw_data) and raw_data[index][0] != "$":
        nodes_to_create.append(raw_data[index])
        index += 1
    return nodes_to_create

for index,command in enumerate(raw_data):
    
    if command == "$ cd /":
        print("creating root directory")
        root_directory = Node("/", None)
        node_pointer = root_directory

    elif command == "$ ls":
        print(f"creating directory: {node_pointer}")
        create_node_list = isolate_nodes_for_creation(index + 1)
        for nodes in  create_node_list:
            node_pointer.add_node(nodes, node_pointer)
        print(node_pointer.children)
    
    elif command == "$ cd ..":
        print("going up a level")
        node_pointer = node_pointer.parent
        print("node_pointer: ", node_pointer)

    elif command[:4] == "$ cd":
        print(f"changing to directory {command.split()[2]}")
        for child in node_pointer.children:
            if child.name == "dir " + command.split()[2]:
                node_pointer = child

node_pointer = root_directory
node_pointer.size()

print(sum([_ for _ in dir_sizes if _ <= 100000]))

total_system_size = 70000000
required_space = 30000000
consumed_space = total_system_size - node_pointer.size
min_delete_required = required_space- consumed_space
print(min([_ for _ in dir_sizes if _ >= min_delete_required]))