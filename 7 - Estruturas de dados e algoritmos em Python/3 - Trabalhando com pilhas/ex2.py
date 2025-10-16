from ex1 import Node

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def pop(self):
    # Check if there is a top element
    if self.top is None:
      return None
    else:
      popped_node = self.top
      # Decrement the size of the stack
      self.size -= 1
      # Update the new value for the top node
      self.top = self.top.next
      popped_node.next = None
      return popped_node.data 
    
'''
O código acima implementa a operação de desempilhar (pop) em uma pilha (stack) usando uma estrutura de dados de lista ligada (linked list) em Python. A função `pop` remove o elemento do topo da pilha, atualiza o ponteiro do topo para o próximo nó na lista, decrementa o tamanho da pilha e retorna o valor do nó removido. Se a pilha estiver vazia, a função retorna `None`.
'''