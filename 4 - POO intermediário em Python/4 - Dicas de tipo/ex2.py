from typing import List

class Agent:
  def __init__(self, codename: str, missions: int):
    self.codename: str = codename
    self.missions: int = missions

  def add_mission(self, location: str) -> None:
    self.missions += 1
    print(f"{self.codename} completed a mission in " + f"{location}. This was mission #{self.missions}")

# Create an Agent object, add type hints
chuck: Agent = Agent("Charles Carmichael", 37)

# Create a list of locations, add a mission for each
locations: List[str] = ["Burbank", "Paris", "Prague"]
for location in locations:
  chuck.add_mission(location)

'''
O código acima demonstra como usar dicas de tipo (type hints) em Python para melhorar a legibilidade e manutenção do código. Ele define uma classe `Agent` com atributos tipados e métodos que também utilizam dicas de tipo. Um objeto `chuck` da classe `Agent` é criado com tipos explícitos, e uma lista de locais é definida com a dica de tipo `List[str]`. O método `add_mission` é chamado para cada local, mostrando como as dicas de tipo ajudam a esclarecer o propósito e o uso das variáveis e métodos no código.
'''