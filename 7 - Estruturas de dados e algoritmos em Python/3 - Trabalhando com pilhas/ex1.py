class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def push(self, data):
    # Create a node with the data
    new_node = Node(data)
    if self.top:
      new_node.next = self.top # type: ignore 
    # Set the created node to the top node
    self.top = new_node
    # Increase the size of the stack by one
    self.size += 1
    
'''
O código acima demonstra como implementar uma pilha (stack) usando uma estrutura de dados de lista ligada (linked list) em Python. A classe `Node` representa um nó na lista ligada, contendo um valor (`data`) e uma referência para o próximo nó (`next`). A classe `Stack` gerencia a pilha, permitindo operações como empilhar (`push`), que adiciona um novo elemento ao topo da pilha.
'''