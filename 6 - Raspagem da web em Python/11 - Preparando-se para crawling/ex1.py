# Get the URL to the website loaded in response
this_url = response.url # type: ignore

# Get the title of the website loaded in response
this_title = response.xpath('/html/head/title/text()').extract_first() # type: ignore

# Print out our findings
print_url_title( this_url, this_title ) # type: ignore


'''
O código acima demonstra como extrair a URL e o título de uma página web usando Scrapy. A função `response.url` obtém a URL atual da página, enquanto a expressão XPath `'/html/head/title/text()'` é usada para extrair o texto do elemento `<title>` dentro do `<head>` do documento HTML. A função `extract_first()` retorna o primeiro resultado encontrado, que é o título da página. Finalmente, a função `print_url_title` é chamada para exibir a URL e o título extraídos.
'''