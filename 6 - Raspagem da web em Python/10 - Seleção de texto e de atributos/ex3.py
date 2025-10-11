from ex2 import html
from scrapy import Selector

def print_results( xpath, css_locator ):
    # Create a selector object from a secret website
    sel = Selector( text=html )

    # Select the text using XPath
    xpath_text = sel.xpath( xpath ).extract()
    print( f"XPath text: {xpath_text}" )

    # Select the text using CSS Locator
    css_text = sel.css( css_locator ).extract()
    print( f"CSS Locator text: {css_text}" )


# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]//text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3 ::text'

# Print the text from our selections
print_results( xpath, css_locator )