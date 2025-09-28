# Import the ABC class and abstractmethod decorator from abc
from abc import ABC, abstractmethod

# Define an abstract base class called Company
class Company(ABC):
  # Create an abstract method called create_budget()
  @abstractmethod
  def create_budget(self):
    pass
  
  # Create a concrete method with name hire_employee()
  def hire_employee(self, name):
    print(f"Welcome to the team, {name}!")

'''
O código acima demonstra como criar uma classe base abstrata em Python usando o módulo abc. A classe Company define um método abstrato create_budget() que deve ser implementado por qualquer subclasse. Além disso, a classe inclui um método concreto hire_employee() que pode ser usado diretamente pelas subclasses. Isso permite que as subclasses herdem a funcionalidade comum enquanto são obrigadas a fornecer suas próprias implementações para os métodos abstratos.
'''