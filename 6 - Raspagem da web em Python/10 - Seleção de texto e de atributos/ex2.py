from scrapy import Selector


html = """
<html>
<body>
<div id="this-div">
<p id="p1" class="class-1">This is not the element you are looking for</p>
<p id="p2" class="class-12">
<a href="https://www.google.com">Google</a> is linked to here, but this isn't the link you are looking for. 
</p>
<p id="p3" class="class-1 class-12">
Here is the <a href="https://www.datacamp.com" id="a-exercise">DataCamp</a> link you want!
</p>
</div>
</body>
</html>"""

# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3::text'

def print_results( xpath, css_locator ):
    # Create a selector object from a secret website
    sel = Selector( text=html )

    # Select the text using XPath
    xpath_text = sel.xpath( xpath ).extract()
    print( f"XPath text: {xpath_text}" )

    # Select the text using CSS Locator
    css_text = sel.css( css_locator ).extract()
    print( f"CSS Locator text: {css_text}" )


# Print the text from our selections
print_results( xpath, css_locator )