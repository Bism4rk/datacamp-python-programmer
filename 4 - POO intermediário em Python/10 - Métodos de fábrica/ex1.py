from abc import ABC, abstractmethod

class Customer(ABC):
  @abstractmethod
  def make_payment(self, price):
    pass

class RewardsMember(Customer):
  def make_payment(self, price):
    print(f"""Total price for rewards member is 
          ${price * .90}, which is 10% off""")

class NewCustomer(Customer):
  def make_payment(self, price):
    print(f"""Total price for new customer is ${price}""")

class Checkout:
  # Create a _get_customer() factory method 
  def _get_customer(self, customer_type):
    if customer_type == "Rewards Member":
      return RewardsMember()
    elif customer_type == "New Customer":
      return NewCustomer()
  
  # Define the complete_transaction() method
  def complete_transaction(self, customer_type, price):
    customer = self._get_customer(customer_type)
    customer.make_payment(price) # type: ignore

'''
O código acima demonstra como implementar métodos de fábrica em Python usando classes abstratas e herança. Ele define uma interface comum para diferentes tipos de clientes (membros de recompensas e novos clientes) e utiliza um método de fábrica para instanciar o tipo correto de cliente com base na entrada fornecida. A classe Checkout gerencia o processo de pagamento, delegando a responsabilidade ao objeto cliente apropriado.
'''