class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_height(node_to_count: BinaryTree):
    if node_to_count is None:
        return 0

    current_left_subtree = count_height(node_to_count.left)
    if current_left_subtree is False:
        return False

    current_right_subtree = count_height(node_to_count.right)
    if current_right_subtree is False:
        return False

    if abs(current_left_subtree - current_right_subtree) > 1:
        return False

    return max(current_left_subtree, current_right_subtree) + 1


def is_tree_balanced(node: BinaryTree) -> bool:
    current_result = count_height(node)

    return current_result is not False
