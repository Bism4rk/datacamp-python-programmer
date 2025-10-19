class TreeNode:
  
  def __init__(self, data, left=None, right=None):
    # Correct the mistakes
    self.data = data
    self.left_child = left
    self.right_child = right

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = TreeNode(data)
    # Check if the BST is empty
    if self.root == None:
      self.root = new_node
      return
    else:
      current_node = self.root
      while True:
        # Check if the data to insert is smaller than the current node's data
        if data < current_node.data:
          if current_node.left_child == None:
            current_node.left_child = new_node
            return 
          else:
            current_node = current_node.left_child
        # Check if the data to insert is greater than the current node's data
        elif data > current_node.data:
          if current_node.right_child == None:
            current_node.right_child = new_node
            return
          else:
            current_node = current_node.right_child

bst = CreateTree() # type: ignore
bst.insert("Pride and Prejudice")
print(search(bst, "Pride and Prejudice")) # type: ignore

'''
O código acima demonstra como implementar uma Árvore de Pesquisa Binária (APB) em Python. Ele define uma classe `BinarySearchTree` com um método `insert` para adicionar novos nós à árvore. A inserção é feita de forma que a propriedade da APB seja mantida: valores menores são colocados à esquerda e valores maiores à direita. No final, o código cria uma instância da árvore, insere um livro e imprime o resultado de uma busca por esse livro. 
'''