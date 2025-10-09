html = """
<html>

  <body>

    <div id="div1" class="class-1">

      <p class="class-1 class-2">Hello World!</p>

      <div id="div2">

        <p id="p2" class="class-2">Choose 

            <a href="http://datacamp.com">DataCamp!</a>!

        </p>

      </div>

    </div>

    <div id="div3" class="class-2">

      <p class="class-2">Thanks for Watching!</p>

    </div>

  </body>

</html>
"""

def print_attribute( xpath ): # Não é parte do exercício original, está aqui para que o código rode
    from lxml import html as lh

    # Parse the HTML string into an lxml object
    doc = lh.fromstring( html )

    # Use the xpath string to select the desired element
    selected_element = doc.xpath( xpath )[0]

    # Print out the text of the selected element
    print("You have selected " + str(selected_element))

# Create an xpath to the href attribute
xpath = '//p[@id="p2"]/a/@href'

# Print out the selection(s); there should be only one
print_attribute( xpath )

'''
O código acima demonstra como xpaths podem ser usados para selecionar atributos específicos de elementos HTML. No exemplo, o xpath '//p[@id="p2"]/a/@href' seleciona o atributo href do elemento <a> que é filho do <p> com id "p2". A função print_attribute então imprime o valor desse atributo, que é "http://datacamp.com".
'''