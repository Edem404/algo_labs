import unittest
from third_lab.src.is_tree_balanced import is_tree_balanced, BinaryTree

root = BinaryTree(1)
first_left = BinaryTree(2)
first_right = BinaryTree(3)
second_left = BinaryTree(4)
second_right = BinaryTree(5)

root.left = first_left
root.right = first_right
first_left.left = second_left
first_left.right = second_right


class TestCase(unittest.TestCase):
    def test_is_balanced(self):
        self.assertEqual(True, is_tree_balanced(root))  # add assertion here

    def test_is_not_balanced(self):
        third_left = BinaryTree(6)
        second_left.left = third_left

        self.assertEqual(False, is_tree_balanced(root))

    def test_without_child(self):
        self.assertEqual(True, is_tree_balanced(second_right))

    def test_is_list_balanced(self):
        root = BinaryTree(1)
        second_element = BinaryTree(2)
        third_element = BinaryTree(3)

        root.left = second_element
        second_element.left = third_element

        self.assertEqual(False, is_tree_balanced(root))

    def test_next_node_balance(self):
        root = BinaryTree(1)
        first_left = BinaryTree(2)
        second_left = BinaryTree(3)
        third_left = BinaryTree(4)

        first_right = BinaryTree(5)
        second_right = BinaryTree(6)
        third_right = BinaryTree(7)

        root.left = first_left
        first_left.left = second_left
        second_left.left = third_left
        root.right = first_right
        first_right = second_right
        second_right.right = third_right

        self.assertEqual(False, is_tree_balanced(root))

    def test_from_machine(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.right.right = BinaryTree(20)
        root.right.right.right = BinaryTree(25)

        self.assertEqual(False, is_tree_balanced(root))


if __name__ == '__main__':
    unittest.main()
