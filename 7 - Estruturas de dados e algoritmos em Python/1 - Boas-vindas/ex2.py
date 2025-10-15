class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def insert_at_beginning(self, data):
    # Create the new node
    new_node = Node(data)
    # Check whether the linked list has a head node
    if self.head:
      # Point the next node of the new node to the head
      new_node.next = self.head
      self.head = new_node
    else:
      self.tail = new_node      
      self.head = new_node

'''
O código acima demonstra como criar uma classe Node em Python para representar um nó em uma estrutura de dados encadeada e uma função para inserir um novo nó no início da lista. A função insert_at_beginning cria um novo nó com o valor fornecido (data) e verifica se a lista já possui um nó cabeça (head). Se houver um nó cabeça, o próximo nó do novo nó é apontado para o nó cabeça existente, e o novo nó se torna o novo nó cabeça. Se a lista estiver vazia, tanto o nó cabeça quanto o nó cauda (tail) são definidos como o novo nó.
'''