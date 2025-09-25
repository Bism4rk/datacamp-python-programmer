class Storage:
  def __init__(self, capacity):
    self.capacity = capacity
  
  def __add__(self, other):  # Overload the + operator
    # Create a Storage object with the sum of capacity
    return Storage(self.capacity + other.capacity)

onboard_storage = Storage(128)
external_drive = Storage(64)

# Add the two Storage objects, show the total capacity
total_storage = onboard_storage + external_drive
print(total_storage.capacity)
  
'''
O código acima demonstra como sobrecarregar o operador de adição (+) em uma classe Python usando um método mágico (__add__). Ele define que a soma de dois objetos da classe Storage resulta em um novo objeto Storage cuja capacidade é a soma das capacidades dos dois objetos originais. No exemplo, dois objetos Storage são criados com capacidades de 128 e 64, respectivamente, e a soma desses objetos resulta em um novo objeto com capacidade total de 192, que é então impressa.
'''