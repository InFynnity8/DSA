# pylint: disable=missing-class-docstring
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return print('Queue is empty')
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return print('Queue is empty')
        return self.queue[0].value
    
    def size(self):
        return len(self.queue) 
    def is_empty(self):
        return len(self.queue) == 0
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
        if trav_type == "levelorder":
            return self.levelorder_traverse(self.root)
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
    def levelorder_traverse(self, start):
        if not start:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while queue.size() > 0:
            node = queue.dequeue()
            traversal += str(node.value) + " -> "
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal


tree = Binary_tree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)

tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)

print('PreOrder')
print(tree.print_traverse("preorder"))
print('InOrder')
print(tree.print_traverse("inorder"))
print('PostOrder')
print(tree.print_traverse("postorder"))
print('LevelOrder')
print(tree.print_traverse("levelorder"))
