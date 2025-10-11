# Select all desired div elements
divs = response.css('div.course-block') # type: ignore

# Take the first div element
first_div = divs[0]

# Extract the text from the (only) h4 element in first_div
h4_text = first_div.css('h4::text').extract_first()

# Print out the text
print( "The text from the h4 element is:", h4_text )

'''
O código acima demonstra como usar seletores CSS para localizar e extrair texto de elementos HTML específicos em uma página web usando Scrapy. Primeiro, ele seleciona todos os elementos `<div>` com a classe `course-block` e armazena-os na variável `divs`. Em seguida, ele acessa o primeiro elemento dessa lista e o armazena em `first_div`. Depois, o código extrai o texto do elemento `<h4>` contido dentro de `first_div` usando o seletor CSS `h4::text` e a função `extract_first()`, que retorna o primeiro resultado encontrado. Finalmente, o texto extraído é impresso no console.
'''