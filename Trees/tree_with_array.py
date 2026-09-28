# Implementation of tree data structure with array.

binary_tree_array = ["R", "A", "B", "C", "D", "E", "F"]

def left_child_index(index):
    return index * 2 + 1

def right_child_index(index):
    return index * 2 + 2

def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None

def pre_order_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order_traversal(left_child_index(index)) + pre_order_traversal(right_child_index(index))

def in_order_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order_traversal(left_child_index(index)) + [binary_tree_array[index]] + in_order_traversal(right_child_index(index))

def post_order_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order_traversal(left_child_index(index)) + post_order_traversal(right_child_index(index)) + [binary_tree_array[index]]


print("Pre order traversal\n", pre_order_traversal(0))
print("In order traversal\n", in_order_traversal(0))
print("Post order traversal\n", post_order_traversal(0))