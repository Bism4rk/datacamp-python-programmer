class Computer:
  def __init__(self, serial_number):
    self.serial_number = serial_number
  
  # Overload the == operator using a magic method
  def __eq__(self, other):
    # Define equality using serial_number
    return self.serial_number == other.serial_number

# Validate two Computers with the same serial_number are equal
first_computer = Computer("81023762")
second_computer = Computer("81023762")
print(first_computer == second_computer)

'''
O código acima demonstra como sobrecarregar o operador de igualdade (==) em uma classe Python usando um método mágico (__eq__). Ele define que dois objetos da classe Computer são considerados iguais se seus atributos serial_number forem iguais. No exemplo, dois objetos Computer são criados com o mesmo número de série, e a comparação usando o operador == retorna True, indicando que eles são iguais de acordo com a definição fornecida no método __eq__.
'''