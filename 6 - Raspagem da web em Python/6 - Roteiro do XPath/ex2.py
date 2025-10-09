from ex1 import html, print_element_text

# Create an XPath string to select p element by class
xpath = '//p[@class="class-1 class-2"]'

# Print out select text
print_element_text( xpath )

'''
O código acima demonstra como xpaths podem ser usados para selecionar elementos específicos com base em atributos como id e class. No exemplo, o xpath '//p[@class="class-1 class-2"]' seleciona o elemento <p> que possui as classes "class-1" e "class-2". A função print_element_text então imprime o texto contido nesse elemento, que é "Hello World!". Note que o uso de aspas duplas dentro do xpath é necessário para evitar conflitos com as aspas simples que delimitam a string do xpath em Python, e que ele só seleciona elementos que possuem exatamente essas duas classes, sem classes adicionais ou em ordem diferente.
'''