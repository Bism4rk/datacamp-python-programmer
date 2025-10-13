# Import the scrapy library
import scrapy


url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names = response.css('p.course-block__author-name::text')
    # Here we will just return the list of Authors
    return author_names
  
def inspect_spider( spider ):
    print(f"You have created a spider named: {spider.name}")

# Inspect the spider
inspect_spider( DCspider )

'''
O código acima demonstra como criar um spider básico usando a biblioteca Scrapy em Python. O spider, chamado "DCspider", inicia uma requisição para uma URL especificada e define um método de callback "parse" para processar a resposta. No método "parse", ele extrai os nomes dos autores dos cursos usando seletores CSS e retorna essa lista de nomes. Finalmente, a função "inspect_spider" é chamada para inspecionar o spider criado. 
'''