class BinarySearchTree:
  def __init__(self):
    self.root = None

  def in_order(self, current_node):
    # Check if current_node exists
    if current_node:
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.left_child)
      # Print the value of the current_node
      print(current_node.data)
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.right_child)
  
bst = CreateTree() # type: ignore // Assuming CreateTree is defined elsewhere
bst.in_order(bst.root)

'''
O código acima demonstra como realizar uma travessia em ordem (in-order traversal) em uma árvore binária de busca (BST) usando a técnica de Depth First Search (DFS). A função `in_order` é chamada recursivamente para visitar o nó esquerdo, imprimir o valor do nó atual e, em seguida, visitar o nó direito. Isso resulta na impressão dos valores da árvore em ordem crescente.
'''