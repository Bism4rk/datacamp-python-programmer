from abc import ABC, abstractmethod

# Create a Product interface
class Product(ABC):
  
  # Define a purchase() abstract method
  @abstractmethod
  def purchase(self, quantity):
    pass
  
  # Create an update_price() abstract method
  @abstractmethod
  def update_price(self, new_price):
    pass

'''
O código acima demonstra como criar uma interface formal em Python usando o módulo `abc`. A classe `Product` é uma interface abstrata que define dois métodos abstratos: `purchase` e `update_price`. Qualquer classe que implemente essa interface deve fornecer definições concretas para esses métodos.
'''