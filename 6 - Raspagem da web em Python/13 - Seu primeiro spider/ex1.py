# Import scrapy library
import scrapy

# Create the spider class
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self): # type: ignore
    pass
  # parse method
  def parse(self, response):
    pass
  
def inspect_class(cls):
    print(f"Class Name: {cls.__name__}")
    print(f"Base Classes: {[base.__name__ for base in cls.__bases__]}")
    print("Methods:")
    for attr in dir(cls):
        if callable(getattr(cls, attr)) and not attr.startswith("__"):
            print(f" - {attr}")
  
# Inspect Your Class
inspect_class(YourSpider)

'''
O código acima demonstra como inspecionar uma classe em Python, especificamente uma classe de spider do Scrapy. A função `inspect_class` imprime o nome da classe, suas classes base e os métodos definidos na classe. Isso é útil para entender a estrutura e os componentes de uma classe personalizada, como um spider do Scrapy.
'''