class Computer:
  def __init__(self, brand):
    self.brand = brand

  def browse_internet(self):
    print(f"Using {self.brand}'s default internet browser.")

class Telephone:
  def __init__(self, phone_number):
    self.phone_number = phone_number

  def make_call(self, recipient):
    print(f"Calling {recipient} from {self.phone_number}")

class Smartphone(Computer, Telephone):
  def __init__(self, brand, phone_number, music_app):
    Computer.__init__(self, brand)
    Telephone.__init__(self, phone_number)
    self.music_app = music_app
    
  def play_music(self, song):
    print(f"Playing {song} using {self.music_app}")

personal_phone = Smartphone("Macrosung", "801-932-7629", "Dotify")

# Browse the internet, make a call to Alex, and play music
personal_phone.browse_internet()
personal_phone.make_call("Alex")
personal_phone.play_music("Creeks and Highways")

'''
O código acima demonstra como a herança múltipla funciona em Python. A classe Smartphone herda atributos e métodos das classes Computer e Telephone, permitindo que um objeto Smartphone utilize funcionalidades de ambas as classes pai. Em seguida, criamos uma instância de Smartphone e utilizamos seus métodos herdados e próprios.
'''
