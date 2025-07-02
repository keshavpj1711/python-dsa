class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
  
  def show_tree(self):
    return (self.left, self.key, self.right)


# Creating a function that creates a tree tuple to tree
# Basic str of this tuple would be: (left_subtree, key, right_subtree)
# Suppose we want to create ((1, 2, 4), 3, (5, 6, None))

def parse_tuple(data):
  if isinstance(data, tuple) and len(data) == 3:
    node = TreeNode(data[1])
    node.left = parse_tuple(data[0])
    node.right = parse_tuple(data[2])
  elif data is None: 
    node = None
  else: 
    node = TreeNode(data)
  
  return node


# Function to trverse tree and change it back to tuple form 
def parse_tree(tree):
  if isinstance(tree, TreeNode): 
    pass



# Displaying tree in much better format
def display_tree(tree, depth=0):
  if tree is None:
    return

  # try to print all nodes of the tree
  if isinstance(tree.left, TreeNode): 
    display_tree(tree.left, depth+1)
  # else: 
  #   print(tree.left, end="\t")

  print(tree.key, end="\t")

  if isinstance(tree.right, TreeNode):
    display_tree(tree.right, depth+1)
  # else:
  #   print(tree.right, end="\t")



tree_tuple = ((1, 2, 4), 3, (5, 6, None))
tree = parse_tuple(tree_tuple)  # This generates trees
display_tree(tree)