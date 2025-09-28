import random

class Lottery:
  def __init__(self, number_digits):
    self.number_digits = number_digits
    self.counter = 0
    
  def __iter__(self):
    return self
  
  # Check if the number of digits have been reached, or else
  # pull another number
  def __next__(self):
    if self.counter < self.number_digits:
      self.counter += 1
      return random.randint(0, 9)

    raise StopIteration

charity_lottery = Lottery(4)

# Announce all four numbers
while True:
  try:
    print(next(charity_lottery))
  
  # Handle the last element of the iterator, print a message
  except StopIteration:
    print("... is the winner!")
    break

'''
O código acima demonstra como criar um iterador customizado em Python usando uma classe chamada Lottery. A classe aceita um número que representa a quantidade de dígitos a serem gerados. Ele implementa os métodos mágicos __iter__() e __next__() para permitir a iteração sobre os dígitos gerados aleatoriamente entre 0 e 9. O exemplo final mostra como usar um loop while para anunciar cada dígito, lidando com a exceção StopIteration quando todos os dígitos tiverem sido gerados.
'''