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

tree_tuple = ((1, 2, 4), 3, (5, 6, None))
tree = parse_tuple(tree_tuple)  # This generates trees


# In-order traversal: We move from left to right basically 
# left -> root -> right
def in_order_traverse(node):
  if node is None:
    return []
  
  return (in_order_traverse(node.left) + [node.key] + in_order_traverse(node.right))

print("In-order Traversed", in_order_traverse(tree))


# Pre-order traversal: 
# root -> left -> right
def pre_order_traverse(node):
  if node is None:
    return []
  
  return ([node.key] + pre_order_traverse(node.left) + pre_order_traverse(node.right))

print("Pre-order Traversed", pre_order_traverse(tree))

# Post-order-traversal
# left -> right -> root
def post_order_traverse(node):
  if node is None:
    return []
  
  return (post_order_traverse(node.left) + post_order_traverse(node.right) + [node.key])

print("Post-order Traversed", post_order_traverse(tree))

