# Create the XPath string equivalent to the CSS Locator 
xpath = '/html/body/span[1]//a'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'html > body > span:nth-of-type(1) a'

# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'

'''
O código acima demonstra as conversões entre seletores XPath e seletores CSS. Ele mostra como selecionar elementos HTML específicos usando ambos os métodos. Por exemplo, o primeiro par de seletores seleciona todos os elementos <a> dentro do primeiro <span> no corpo do documento HTML. O segundo par de seletores seleciona todos os elementos <h4> que são descendentes de um <span> dentro de um <div> com o ID "uid".
'''