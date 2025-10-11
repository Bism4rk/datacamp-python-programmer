# Create a CSS Locator string to the desired hyperlink elements
css_locator = 'a.course-block__link'

# Select the hyperlink elements from response and sel
response_as = response.css(css_locator) # type: ignore
sel_as = sel.css(css_locator) # type: ignore

# Examine similarity
nr = len( response_as )
ns = len( sel_as )
for i in range( min(nr, ns, 2) ):
  print( "Element %d from response: %s" % (i+1, response_as[i]) )
  print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
  print( "" )

'''
O código acima demonstra como usar seletores CSS para localizar elementos de hyperlink em uma página web. A variável `css_locator` contém a string do seletor CSS que identifica os elementos desejados, neste caso, links com a classe `course-block__link`. As funções `response.css()` e `sel.css()` são usadas para selecionar esses elementos tanto do objeto `response` quanto do objeto `sel`. Em seguida, o código compara os primeiros dois elementos encontrados em ambos os objetos, imprimindo-os para análise. Isso é útil para verificar a consistência entre diferentes métodos de seleção de elementos em uma página web.
'''