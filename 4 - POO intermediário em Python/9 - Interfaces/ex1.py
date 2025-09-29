class Supplier:
  def take_order(self, product_name, quantity):
    pass

  def make_delivery(self, order_id, location):
    pass

class YogurtSupplier:
  def __init__(self):
    self.orders = {}
  
  # Finish defining the take_order() method
  def take_order(self, product_name, quantity):
    self.orders[f"{product_name}_{quantity}"] = {
      "product_name": product_name, "quantity": quantity
    }
  
  # Implement a make_delivery() abstract method
  def make_delivery(self, order_id, location):
    print(f"Delivering order: {order_id} to {location}")
    del self.orders[order_id]

'''
O código acima demonstra como implementar uma interface informal em Python. A classe `Supplier` define a interface com dois métodos: `take_order` e `make_delivery`. A classe `YogurtSupplier` implementa essa interface, fornecendo definições concretas para ambos os métodos.
'''