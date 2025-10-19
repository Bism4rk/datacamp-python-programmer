import queue

class ExpressionTree:
  def __init__(self):
    self.root = None

  def pre_order(self, current_node):
    # Check if current_node exists
    if current_node:
      # Print the value of the current_node
      print(current_node.data)
      # Call pre_order recursively on the appropriate half of the tree
      self.pre_order(current_node.left_child)
      self.pre_order(current_node.right_child)

          
et = CreateExpressionTree() # type: ignore // Assuming CreateExpressionTree is defined elsewhere
et.pre_order(et.root)

'''
O código acima demonstra como realizar uma travessia em pré-ordem (pre-order traversal) em uma árvore de expressão usando a técnica de Depth First Search (DFS). A função `pre_order` é chamada recursivamente para imprimir o valor do nó atual, visitar o nó esquerdo e, em seguida, visitar o nó direito. Isso resulta na impressão dos valores da árvore na ordem em que são encontrados, começando pela raiz.
'''