class Computer:
  def __init__(self, brand):
    self.brand = brand

  def browse_internet(self):
    print(f"Using {self.brand}'s default internet browser.")

class Tablet(Computer):
  def __init__(self, brand, apps):
    Computer.__init__(self, brand)
    self.apps = apps

  def uninstall_app(self, app):
    if app in self.apps:
      self.apps.remove(app)

# Create a Smartphone class that inherits from Tablet
class Smartphone(Tablet):
  def __init__(self, brand, apps, phone_number):
    Tablet.__init__(self, brand, apps)
    self.phone_number = phone_number
  
  # Create send_text to send a message to a recipient
  def send_text(self, message, recipient):
    print(f"Sending {message} to {recipient} from {self.phone_number}")

# Create an instance of Smartphone, call methods in each class
personal_phone = Smartphone("Macrosung", ["Weather", "Camera"], "801-932-7629")    
personal_phone.browse_internet()
personal_phone.uninstall_app("Weather")
personal_phone.send_text("Time for a new mission!", "Chuck")

'''
O código acima demonstra como a herança múltipla funciona em Python. A classe Smartphone herda atributos e métodos das classes Tablet e Computer, permitindo que um objeto Smartphone utilize funcionalidades de ambas as classes pai. Em seguida, criamos uma instância de Smartphone e utilizamos seus métodos herdados e próprios.
'''