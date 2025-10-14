# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

url_short = "https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short"

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    # Create a SelectorList of the course titles text
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    # Extract the text and strip it clean
    crs_title_ext = crs_title.extract_first().strip()
    # Create a SelectorList of course descriptions text
    crs_descr = response.css( 'p.course__description::text' )
    # Extract the text and strip it clean
    crs_descr_ext = crs_descr.extract_first().strip()
    # Fill in the dictionary
    dc_dict[crs_title_ext] = crs_descr_ext

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
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)

'''
O código acima demonstra como criar um spider Scrapy para raspar descrições de cursos do site DataCamp. Ele define uma classe de spider chamada `DC_Description_Spider`, que inicia a raspagem a partir de uma URL curta fornecida. O método `start_requests` envia uma solicitação para essa URL e chama o método `parse_front` para processar a resposta. O método `parse_front` extrai os links dos cursos da página inicial e segue cada link, chamando o método `parse_pages` para cada página de curso. O método `parse_pages` extrai o título do curso e a descrição do curso, armazenando-os em um dicionário `dc_dict`. Após a execução do spider, a função `previewCourses` é chamada para exibir uma prévia dos cursos e suas descrições.
'''