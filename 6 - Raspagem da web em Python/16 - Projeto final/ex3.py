# Import scrapy
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

url_short = "https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short"

# Create the Spider class
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request(url = url_short, callback=self.parse)
      
  def parse(self, response):
    # My version of the parser you wrote in the previous part
    crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
    crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
    for crs_title, crs_descr in zip( crs_titles, crs_descrs ):
      dc_dict[crs_title] = crs_descr
    
# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

def previewCourses(dc_dit, n=3):
    for i, (k,v) in enumerate(dc_dit.items()):
        if i >= n:
            break
        print(f"{k}:")
        print(f"  - {v}")

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)

'''
O código acima demonstra como criar um spider Scrapy para raspar títulos e descrições de cursos do site DataCamp. Ele define uma classe de spider chamada `YourSpider`, que inicia a raspagem a partir de uma URL curta fornecida. O método `start_requests` envia uma solicitação para essa URL e chama o método `parse` para processar a resposta. O método `parse` extrai os títulos e descrições dos cursos da página inicial, armazenando-os em um dicionário `dc_dict`. Após a execução do spider, a função `previewCourses` é chamada para exibir uma prévia dos cursos e suas descrições.
'''