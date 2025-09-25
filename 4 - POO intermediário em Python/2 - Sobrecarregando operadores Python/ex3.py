class Network:
  def __init__(self, ip_addresses):
    self.ip_addresses = ip_addresses

class Computer:
  def __init__(self, operating_system, ip_address):
    self.operating_system = operating_system
    self.ip_address = ip_address
    
    def __add__(self, other):
        if self.operating_system == other.operating_system:
            return Network([self.ip_address, other.ip_address])
    raise Exception("Incompatible operating systems.")

# Build a network using Morgan and Jenny's Computers
morgans_computer = Computer("Windows", "182.112.81.991")
jennys_computer = Computer("Windows", "177.511.64.162")
network = morgans_computer + jennys_computer
