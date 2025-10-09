# an html string with a bunch of links with the class "dropdown__link"
html = """
<html>
  <body>
    <div class="dropdown">
      <a class="dropdown__link" href="http://funnysite.com">Link 1</a>
      <a class="dropdown__link" href="http://farfetchdcomedyhour.com">Link 2</a>
      <a class="dropdown__link" href="http://notasuspiciouslinkatallnuhuhnotafrontforiceatall.gov">Link 3</a>
    </div>
  </body>
</html>
"""

def how_many_elements( xpath ): # Não é parte do exercício original, está aqui para que o código rode
    from lxml import html as lh

    # Parse the HTML string into an lxml object
    doc = lh.fromstring( html )

    # Use the xpath string to select the desired elements
    selected_elements = doc.xpath( xpath )

    # Print out how many elements were selected
    print( "You have selected " + str(len(selected_elements)) + " elements." )

def preview( xpath ): # Não é parte do exercício original, está aqui para que o código rode
    from lxml import html as lh

    # Parse the HTML string into an lxml object
    doc = lh.fromstring( html )

    # Use the xpath string to select the desired elements
    selected_elements = doc.xpath( xpath )

    # Print out a preview of the selected elements
    print( "Here is a preview of the selected elements: " + str(selected_elements[:5]) )

# Create an xpath to the href attributes
xpath = '//a[contains(@class,"dropdown__link")]/@href'

# Print out how many elements are selected
how_many_elements( xpath )
# Preview the selected elements
preview( xpath )

'''
O código acima demonstra como xpaths podem ser usados para selecionar múltiplos elementos com base em um atributo comum. No exemplo, o xpath '//a[contains(@class,"dropdown__link")]/@href' seleciona o atributo href de todos os elementos <a> que possuem a classe "dropdown__link". A função how_many_elements então imprime quantos elementos foram selecionados, que é 3, e a função preview imprime uma prévia dos elementos selecionados, que são os três links fornecidos no HTML.
'''