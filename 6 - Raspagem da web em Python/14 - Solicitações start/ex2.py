# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url="https://www.datacamp.com", callback=self.parse )
  # parse method
  def parse( self, response ):
    pass
  
def inspect_class(cls):
    # Get the first request from the generator
    first_request = next(cls.start_requests(cls()))
    print(f"The URL you would scrape is: {first_request.url}")

# Inspect Your Class
inspect_class( YourSpider )

'''
O código acima demonstra como criar uma classe de aranha personalizada em Scrapy, incluindo métodos para iniciar solicitações e analisar respostas. A função inspect_class é usada para inspecionar a URL que a aranha tentaria raspar ao chamar o método start_requests.
'''