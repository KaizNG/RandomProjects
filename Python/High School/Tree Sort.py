class Node:
  def __init__(self, rootvalue):
    self.value = rootvalue
    self.left = None
    self.right = None

  def setLeft(left, node):
    left.left = node

  def setRight(right, node):
    right.right = node

  def insertNum(self, value):
    if self.value:
      if value < self.value:
        if self.left is None:
          self.setLeft(Node(value))
        else:
          self.left.insertNum(value)

      elif value > self.value:
        if self.right is None:
          self.setRight(Node(value))
        else:
          self.right.insertNum(value)T
