from html2 import html
from scrapy import Selector

# Create a selector from the html (of a secret website)
sel = Selector( text=html )

def how_many_elements( css_locator ):
    """Print the number of elements matching the css_locator"""
    print( "There are 20 course blocks on the page." )
    print( "You have found: ", len( sel.css( css_locator ) ) )

# Fill in the blank
css_locator = "div.course-block > a"

# Print the number of selected elements.
how_many_elements( css_locator )

'''
O código acima demonstra como usar seletores CSS para contar o número de elementos específicos em um documento HTML. Ele utiliza a biblioteca Scrapy para criar um seletor a partir do HTML fornecido e define uma função que conta e imprime o número de elementos que correspondem a um determinado seletor CSS. No exemplo, o seletor "div.course-block > a" é usado para selecionar todos os elementos <a> que são filhos diretos de elementos <div> com a classe "course-block". A função então imprime o número total de elementos encontrados, comparando-o com o número esperado (20 blocos de curso na página).
'''