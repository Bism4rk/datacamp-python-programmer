def whats_my_class( html ):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup( html, 'html.parser' )
    divs = soup.find_all( 'div' )
    print("The class you assigned the second div element to is " +  str(divs[1]['class'])) # type: ignore

# HTML code string
html = '''
<html>
  <body>
    <div class="class1" id="div1">
      <p class="class2">Visit DataCamp!</p>
    </div>
    <div class="you-are-classy">
      <p class="class2">Keep up the good work!</p>
    </div>
  </body>
</html>
'''
# Print out the class of the second div element
whats_my_class( html )

'''
O código acima demonstra classes HTML. A função whats_my_class usa BeautifulSoup para analisar uma string HTML e encontrar todos os elementos <div>. Em seguida, imprime a classe atribuída ao segundo elemento <div>.
'''