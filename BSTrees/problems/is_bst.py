# Ok so this is going to be about if the binary tree that is the input is a binary search tree or not

# Now talking of the basic contraints the left subtree should have smaller values than the key 
# and the right one has larger vals 

# But when implementing this major thing to keep in mind is that:
# We need to also keep in check with the ancestors of the node 
# therefor the signature of the fn also includes the max/min(depending on left or right) value it can have 

from warnings import resetwarnings


class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

# Creating our tree
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

tree_tuple = (((0, 1, None), 2, 4), 3, (5, 6, None))
tree = parse_tuple(tree_tuple)  # This generates trees

tree_tuple1 = (2, 3, 4)
tree1 = parse_tuple(tree_tuple1)  # This generates trees

tree_tuple2 = (4, 3, 2)
tree2 = parse_tuple(tree_tuple2)  # This generates trees


def is_valid_bst(node, max_value=None, min_value=None):
  # Base case
  if node is None:
    return True  # so this means that we never found any errors in this bt
  
  if max_value is not None:
    print("Checking with max val")
    if node.key >= max_value:
      print(f"False printed for {node.key}")
      return False
  
  if min_value is not None:
    print("Checking with min val")
    if node.key <= min_value:
      print(f"False printed for {node.key}")
      return False
  
  result = is_valid_bst(node.left, max_value=node.key, min_value=min_value) and is_valid_bst(node.right, min_value=node.key, max_value=max_value)
  return result


def get_max_min(node):
  def in_order_traversal(node):
    if node is None:
      return []

    return (in_order_traversal(node.left) + [node.key] + in_order_traversal(node.right))

  result = in_order_traversal(node)
  if result:
    return (result[0], result[-1])
  else:
    return 
  

def get_max_min_opt(node):
  if node is None:
    return None

  def find_min(node):
    if node.left == None:
      return node.key

    return find_min(node.left)

  def find_max(node):
    if node.right == None:
      return node.key

    return find_max(node.right)

  return (find_min(node), find_max(node))
      


print(is_valid_bst(tree))
print("Max, min values: ", get_max_min(tree))
print("Max, min values: ", get_max_min_opt(tree))
print()
print(is_valid_bst(tree1))
print()
print(is_valid_bst(tree2))
print()
