"""
[unfinished]
1) Create the Binary Search Tree Class and a Node Class
2) Implement the Search Method in the BST with True/False
3) Implement the Insertion Method in the BST
4) How would you delete a node? What to think about???
5) How would you traverse through it … create a method that helps us print the tree. (There are 3 types: pre-order, post-order, in-order)
6) Return a sorted list from BST method
"""



class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def setLeft(self, left):
    self.left = left

  def setRight(self, right):
    self.right = right

  def displayValue(self):
    print(self.value)

new = Node(6)

root = Node(5)
class Tree:
  def __init__(self,root):
    self.root = root

  def Insert(self, node):
    pass

tree = Tree(root)
