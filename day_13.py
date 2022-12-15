pair_list = [[*map(eval, x.split())] for x in open('advent_of_code_2022\day_13_input.txt').read().split('\n\n')]

# Recursive function that checks if two elements are in order based on certain rules. 

# if inputs are of different types int and list, convert the int to list and rerun the comparison

# if both inputs are of type int:
#   return True if first element is less than the second element
#   if both elements are equal return None

# if both elements are of type list:
#   zip both lists together and rerun comparison on each zipped pair
#       for example, list_1 = [1,1,2,3] list_2 = [1,1,3,4]
#       zipped_list = [(1,1),(1,1),(2,3),(3,4)]
#       running comparison on each pair:
#           sub_list_comparison = list_comp(1,1) = None
#           sub_list_comparison = list_comp(1,1) = None
#           sub_list_comparison = list_comp(2,3) = True
#       in this case list_comp returned True for the third zipped pair, the lists are in order
#       if for example the zipped pair was (4,2); list_comp(4,2) would have returned False meaning the lists are out of order
#   
#   IF LISTS ARE UNEQUAL LENGTH: THE FIRST LIST MUST BE SHORTER THAN THE SECOND
#       this is done by running list_comp(len(element_1), len(element_2)) after all zipped pairs have returned None because they are equal
#       if this returns None as well, the lists are identical
def list_comp(element_1, element_2):
    if type(element_1) == int and type(element_2) == int:
        if element_1 == element_2:
            return None
        return element_1 < element_2
    if type(element_1) == int and type(element_2) == list:
        return list_comp([element_1], element_2)
    if type(element_1) == list and type(element_2) == int:
        return list_comp(element_1, [element_2])
    if type(element_1) == list and type(element_2) == list:
        for sub_list_1,sub_list_2 in zip(element_1, element_2):
            sub_list_comparison = list_comp(sub_list_1, sub_list_2)
            if sub_list_comparison is not None: 
                return sub_list_comparison
        return list_comp(len(element_1), len(element_2))

# problem one. Sum of indexes(starting at one) of the in order packets
# packets are considered in order if the return value for list_comp is True
index_sum = 0
for index,pair in enumerate(pair_list,1):
    if list_comp(*pair) == True:
        index_sum += index
print(index_sum)

# problem two. Position of decoder packets [[2]] and [[6]] after sorting all packets
# add decoder packets
# unpack pairs from the first problem into a list of individual packets
pair_list = sum(pair_list,[[6],[2]])
# store the result of comparison for neighbouring packets
comp_values = [False for _ in range(len(pair_list)-1)]
# while the result of neighbouring comparison is False, swap packets
while comp_values.count(True) != len(comp_values):
    for index in range(1,len(pair_list)):
        comp_values[index-1] = list_comp(pair_list[index-1],pair_list[index])
        if not comp_values[index-1]:
            pair_list[index-1],pair_list[index] = pair_list[index],pair_list[index-1]
# print product of indices(starting at 1) of packets [[2]] and [[6]]
print((pair_list.index([2])+1) * (pair_list.index([6])+1))