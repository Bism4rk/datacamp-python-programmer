class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def remove_at_beginning(self):
    # The "next" node of the head becomes the new head node
    self.head = self.head.next # type: ignore

'''
O código acima demonstra como criar uma classe Node em Python para representar um nó em uma estrutura de dados encadeada e uma classe LinkedList para gerenciar a lista encadeada. A classe LinkedList possui um construtor (__init__) que inicializa os atributos head e tail como None, representando o início e o fim da lista. A função remove_at_beginning atualiza o nó cabeça (head) para apontar para o próximo nó na lista, efetivamente removendo o nó atual do início da lista.
'''