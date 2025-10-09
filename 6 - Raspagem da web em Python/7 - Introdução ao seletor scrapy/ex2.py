from scrapy import Selector

html = """
<html>
<body>
<div>Div 1: <p>paragraph 1</p></div>
<div>Div 2: <p>paragraph 2</p> <p>paragraph 3</p> </div>
<div>Div 3: <p>paragraph 4</p> <p>paragraph 5</p> <p>paragraph 6</p></div>
<div>Div 4: <p>paragraph 7</p></div>
<div>Div 5: <p>paragraph 8</p></div>
</body>
</html>"""

# Create a Selector selecting html as the HTML document
sel = Selector( text=html )

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( '//div' )

'''
O código acima demonstra como usar o Scrapy Selector para analisar um documento HTML e selecionar todos os elementos <div> presentes nele. Ele cria um SelectorList contendo esses elementos, permitindo manipulação e extração de dados subsequentes.
'''