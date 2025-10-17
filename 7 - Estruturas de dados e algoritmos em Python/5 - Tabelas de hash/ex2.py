my_menu = {

  'sushi' : {
    'price' : 19.25,
    'best_served' : 'cold'
  },

  'paella' : {
    'price' : 15,
    'best_served' : 'hot'
  },

  'samosa' : {
    'price' : 14,
    'best_served' : 'hot'
  },

  'gazpacho' : {
    'price' : 8,
    'best_served' : 'cold'
  }

}

# Iterate the elements of the menu
for dish, values in my_menu.items():
  # Print whether the dish must be served cold or hot
  print(f"{dish.title()} is best served {values['best_served']}.")

'''
O código acima demonstra como iterar sobre um dicionário aninhado em Python. Cada prato do menu é uma chave no dicionário principal, e o valor associado a cada chave é outro dicionário que contém informações adicionais sobre o prato, como preço e a melhor forma de servi-lo. Durante a iteração, o código acessa essas informações e imprime uma mensagem indicando se o prato deve ser servido quente ou frio.
'''