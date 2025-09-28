from abc import ABC, abstractmethod

class Company(ABC):
  @abstractmethod
  def pay_taxes(self):
    pass
  
  def report_revenue(self):
    print(f"{self.name} is reporting ${self.revenue} of revenue") # type: ignore


class Manufacturing(Company):
  def __init__(self, name, revenue):
    self.name = name
    self.revenue = revenue

  def pay_taxes(self, tax_rate): # type: ignore
    tax_amount = self.revenue * tax_rate
    print(f"{self.name} is paying ${tax_amount} of taxes")

# Create an instance of the Manufacturing class
m = Manufacturing("Morgan's Manufacturing", 5000)

# Make call to the pay_taxes() method, observe report_revenue()
m.pay_taxes(.10)
m.report_revenue()

'''
O código acima demonstra como criar uma subclasse da classe base abstrata Company. A classe Manufacturing implementa o método abstrato pay_taxes() e fornece sua própria lógica para calcular e relatar os impostos. Além disso, a classe herda o método report_revenue() da classe base, permitindo que os objetos Manufacturing utilizem essa funcionalidade sem precisar reimplementá-la.
'''