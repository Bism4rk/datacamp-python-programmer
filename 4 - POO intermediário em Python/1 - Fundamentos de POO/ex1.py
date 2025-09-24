class Computer:
  def __init__(self, storage):
    self.storage = storage

  def add_external_drive(self, external_storage):
    self.storage += external_storage
    print(f"Your computer now has {self.storage} GB of storage.")

  @classmethod
  def power_on(cls):
    print("Your computer is starting up!")

my_computer = Computer(512)

# Add an external drive of 256 GB
my_computer.add_external_drive(256)

'''
O código acima demonstra como definir uma classe em Python com um método de instância e um método de classe. O método de instância `add_external_drive` modifica o estado do objeto, enquanto o método de classe `power_on` é chamado na classe em si e não depende do estado de uma instância específica.
'''