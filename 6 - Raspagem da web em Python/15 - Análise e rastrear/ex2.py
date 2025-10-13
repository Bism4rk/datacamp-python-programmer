# Import the scrapy library
import scrapy
from ex1 import url_short

# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow(url=link, callback=self.parse_descr)
      
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    yield course_descr


def inspect_spider( spider ):
    print(f"You have created a spider named: {spider.name}")
    print(f"The spider starts making requests from: {spider.start_requests().__next__().url}")

# Inspect the spider
inspect_spider( DCdescr )

'''
O código acima demonstra como criar um spider mais avançado usando a biblioteca Scrapy em Python. O spider, chamado "DCdescr", inicia uma requisição para uma URL especificada e define um método de callback "parse" para processar a resposta inicial. No método "parse", ele extrai links de cursos e segue cada link, chamando o método "parse_descr" para cada página de curso. No método "parse_descr", ele extrai a descrição do curso e a retorna. A função "inspect_spider" é chamada para inspecionar o spider criado, exibindo seu nome e a URL inicial de requisição.
'''