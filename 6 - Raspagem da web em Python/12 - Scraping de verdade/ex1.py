import requests
from scrapy import Selector

response = requests.get('https://www.datacamp.com/courses/all')
selector = Selector(text=response.text)

# Create a SelectorList of the course titles
crs_title_els = selector.css('h4::text') # type: ignore

# Extract the course titles 
crs_titles = crs_title_els.extract()

# Print out the course titles 
for el in crs_titles:
  print( ">>", el )

'''
O código acima demonstra como usar a biblioteca Scrapy para raspar títulos de cursos de uma página web. Ele faz o seguinte:
1. Importa as bibliotecas necessárias: requests para fazer requisições HTTP e Selector do Scrapy para analisar o HTML.
2. Faz uma requisição GET para a URL da página de cursos da DataCamp.
3. Cria um objeto Selector a partir do conteúdo da resposta.
4. Usa seletores CSS para extrair os títulos dos cursos.
5. Imprime os títulos dos cursos.
'''