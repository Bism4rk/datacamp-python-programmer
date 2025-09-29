from abc import ABC, abstractmethod

class Business(ABC):
  @abstractmethod
  def sell_product(self, product_name, price, quantity):
    pass

# Create a class that inherits the Business interface
class Bakery(Business): # type: ignore
  def __init__(self, business_name):
    self.business_name = business_name

# Attempt to create a Bakery object, observe the exception
try:
  blue_eyed_baker = Bakery("Blue Eyed Baker") # type: ignore
except Exception as e:
  print(e)

class Bakery(Business):
  def __init__(self, business_name):
    self.business_name = business_name
  
  # Provide a definition of the sell_product() method 
  def sell_product(self, product_name, price, quantity):
    total_revenue = price * quantity
    print(f"""{self.business_name} sold {quantity} 
          {product_name} for a total of ${total_revenue}""")
    
# Attempt to create a Bakery object
blue_eyed_baker = Bakery("Blue Eyed Baker")

'''
O código acima demonstra como criar uma interface formal em Python usando o módulo `abc` e como implementar essa interface em uma classe concreta. A classe `Business` é uma interface abstrata que define o método abstrato `sell_product`. A classe `Bakery` herda dessa interface e fornece uma implementação concreta do método `sell_product`. A tentativa inicial de criar um objeto da classe `Bakery` sem implementar o método abstrato resulta em uma exceção, que é capturada e exibida. Após a implementação do método, a criação do objeto `blue_eyed_baker` é bem-sucedida.
'''