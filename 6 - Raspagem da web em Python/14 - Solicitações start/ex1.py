# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ): # type: ignore
    self.print_msg( 'Hello World!' )
  # parse method
  def parse( self, response ):
    pass
  # print_msg method
  def print_msg( self, msg ):
    print( "Calling start_requests in YourSpider prints out:", msg )
  
def inspect_class( cls ):
    print( "\nClass name:", cls.__name__ )
    print( "Base classes:", cls.__bases__ )
    print( "Attributes and methods:", dir( cls ) )

# Inspect Your Class
inspect_class( YourSpider )

'''
O código acima demonstra como criar uma classe de aranha personalizada em Scrapy, incluindo métodos para iniciar solicitações, analisar respostas e imprimir mensagens. A função inspect_class é usada para inspecionar a estrutura da classe, exibindo seu nome, classes base e atributos/métodos disponíveis.
'''