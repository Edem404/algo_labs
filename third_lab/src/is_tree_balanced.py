class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_height(node_to_count: BinaryTree):
    if node_to_count is None:
        return 0

    current_left_subtree = node_to_count.left
    current_right_subtree = node_to_count.right

    return max(count_height(current_left_subtree), count_height(current_right_subtree)) + 1


def is_tree_balanced(node: BinaryTree) -> bool:
    is_balanced = True

    if node is None:
        return is_balanced

    height_left_subtree = count_height(node.left)
    height_right_subtree = count_height(node.right)

    if abs(height_left_subtree - height_right_subtree) <= 1:

        is_tree_balanced(node.left)
        is_tree_balanced(node.right)
        return is_balanced
    else:
        is_balanced = False
        return is_balanced


root = BinaryTree(1)
first_left = BinaryTree(2)
first_right = BinaryTree(3)
second_left = BinaryTree(4)
second_right = BinaryTree(5)
third_left = BinaryTree(6)
fourth_right = BinaryTree(7)

root.left = first_left
root.right = first_right
first_left.left = second_left
first_left.right = second_right
second_left.left = third_left
first_right.right = fourth_right

print(is_tree_balanced(root))
