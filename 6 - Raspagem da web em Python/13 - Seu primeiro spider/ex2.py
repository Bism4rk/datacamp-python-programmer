# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ['https://www.datacamp.com', 'https://scrapy.org']
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass
  
def inspect_class( cls ):
    print(f"The start_requests method yields the following URLs: {list(cls().start_requests())}")

# Inspect Your Class
inspect_class( YourSpider )

'''
O código acima define uma classe de spider do Scrapy chamada `YourSpider`, que inclui um método `start_requests` que gera uma lista de URLs. A função `inspect_class` instancia a classe e imprime as URLs geradas pelo método `start_requests`. Isso demonstra como criar um spider básico e inspecionar seu comportamento em Python.
'''