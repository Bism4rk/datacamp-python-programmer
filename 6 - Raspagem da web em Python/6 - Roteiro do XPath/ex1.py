html = """
<html>

  <body>

    <div id="div1" class="class-1">

      <p class="class-1 class-2">Hello World!</p>

      <div id="div2">

        <p id="p2" class="class-2">Choose DataCamp!</p>

      </div>

    </div>

    <div id="div3" class="class-2">

      <p class="class-2">Thanks for Watching!</p>

    </div>

  </body>

</html>"""

def print_element_text( xpath ): # Não é parte do exercício original, está aqui para que o código rode
    from lxml import html as lh

    # Parse the HTML string into an lxml object
    doc = lh.fromstring( html )

    # Use the xpath string to select the desired element
    selected_element = doc.xpath( xpath )[0]

    # Print out the text of the selected element
    print( selected_element.text )


# Create an Xpath string to select desired p element
xpath = '//*[@id="div3"]/p'

# Print out selection text
print_element_text( xpath )

'''
O código acima demonstra como xpaths podem ser usados para selecionar elementos específicos com base em atributos como id e class. No exemplo, o xpath '//*[@id="div3"]/p' seleciona o elemento <p> que é filho do <div> com id "div3". A função print_element_text então imprime o texto contido nesse elemento, que é "Thanks for Watching!".
'''