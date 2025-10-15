class Node:
  def __init__(self, data):
    # Store the value for the node
    self.value = data
    # Leave the node initially without a next value
    self.next = None
    # Set the head and the tail with null values
    self.head = None
    self.tail = None

'''
O código acima demonstra como criar uma classe Node em Python para representar um nó em uma estrutura de dados encadeada. A classe possui um construtor (__init__) que inicializa o valor do nó (data) e define o próximo nó (next) como None. Além disso, a classe também possui atributos head e tail, que são inicialmente definidos como None, para representar o início e o fim da estrutura de dados.
'''