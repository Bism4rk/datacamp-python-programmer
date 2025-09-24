class Computer:
  def __init__(self, software_version):
    self.software_version = software_version

  def install_app(self, app_name, app_store):
    if app_store:
      print(f"Installing {app_name} from App Store.")
    else:
      print(f"Installing {app_name} from other provider.")

  def update_software(self, new_software_version):
      self.software_version = new_software_version

class Tablet(Computer):
  pass

# Create the my_tablet instance
my_tablet = Tablet("1.1.1")

# Update my_tablet's software to version 1.1.2
my_tablet.update_software("1.1.2")
print(my_tablet.software_version)

class Tablet(Computer):
  # Override the install_app() method
  def install_app(self, app_name):
    print(f"{app_name} is being installed from the Tablet App Store.")
    
my_tablet = Tablet("1.1.1")

# Call the new install_app() method
my_tablet.install_app("DataCamp")

'''
O código acima demonstra como criar uma subclasse em Python que herda de uma superclasse. A subclasse `Tablet` herda os atributos e métodos da classe `Computer`, e também pode sobrescrever métodos para fornecer implementações específicas, como o método `install_app`.
'''

