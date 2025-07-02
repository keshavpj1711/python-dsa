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

tree_tuple = (((0, 1, 5), 2, 4), 3, (5, 6, None))
tree = parse_tuple(tree_tuple)  # This generates trees


def get_tree_size(node):
  # base case
  if node is None:
    return 0
  
  # returning size for left, right and current node(this is 1)
  return get_tree_size(node.left) + get_tree_size(node.right) + 1
  

def get_tree_depth(node):
  # base case
  if node is None:
    return 0
  
  return max((get_tree_depth(node.left) + 1), (get_tree_depth(node.right) + 1))


print("Number of nodes: ", get_tree_size(tree))
print("Tree Depth: ", get_tree_depth(tree))