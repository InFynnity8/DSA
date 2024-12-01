# pylint: disable=missing-class-docstring
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_traverse(self, trav_type):
        if trav_type == "inorder":
            return self.inorder_traverse(self.root, "")
        if trav_type == "preorder":
            return self.preorder_traverse(self.root, "")
        if trav_type == "postorder":
            return self.postorder_traverse(self.root, "")
        return print(
            "Invalid traversal type. Choose from inorder, preorder, or postorder."
        )

    def preorder_traverse(self, start, traversal):
        if start:
            traversal += str(start.value) + " -> "
            traversal = self.preorder_traverse(start.left, traversal)
            traversal = self.preorder_traverse(start.right, traversal)
        return traversal

    def inorder_traverse(self, start, traversal):
        if start:
            traversal = self.inorder_traverse(start.left, traversal)
            traversal += str(start.value) + " -> "
            traversal = self.inorder_traverse(start.right, traversal)
        return traversal

    def postorder_traverse(self, start, traversal):
        if start:
            traversal = self.postorder_traverse(start.left, traversal)
            traversal = self.postorder_traverse(start.right, traversal)
            traversal += str(start.value) + " -> "
        return traversal


tree = Binary_tree(0)
tree.root.left = TreeNode(5)
tree.root.right = TreeNode(7)

tree.root.left.left = TreeNode(6)
tree.root.left.right = TreeNode(9)

tree.root.right.left = TreeNode(3)
tree.root.right.right = TreeNode(13)

print('PreOrder')
print(tree.print_traverse("preorder"))
print('InOrder')
print(tree.print_traverse("inorder"))
print('PostOrder')
print(tree.print_traverse("postorder"))
