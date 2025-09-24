class Computer:
  def __init__(self, device_id, storage):
    self.device_id = device_id
    self.storage = storage
  
  # Overload the == operator using a magic method
  def __eq__(self, other):
    # Return a boolean based on the value of device_id
    return self.device_id == other.device_id

pre_upgrade_computer = Computer("Y391Hky6", 256)
post_upgrade_computer = Computer("Y391Hky6", 1024)

# Create two instances of Computer, compare using ==
print(pre_upgrade_computer == post_upgrade_computer)

'''
O código acima demonstra como sobrecarregar o operador de igualdade (==) em uma classe Python, permitindo que duas instâncias da classe sejam comparadas com base em um atributo específico (neste caso, device_id).
'''