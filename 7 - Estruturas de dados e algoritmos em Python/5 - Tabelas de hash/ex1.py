'''
Código original:

for key, value in my_menu():
  # Correct the mistake
  print(f"The price of the {value} is {key}.")
'''
my_menu = {
  'lasagna': 14.75,
  'moussaka': 21.15,
  'sushi': 16.05,
  'paella': 21,
  'samosas': 14
}

# Correct the mistake
for key, value in my_menu.items():
  # Correct the mistake
  print(f"The price of the {key} is {value}.")

'''
O código acima demonstra como iterar corretamente sobre um dicionário em Python usando o método items(). Cada par chave-valor do dicionário é acessado, e a mensagem correta é impressa formatando a string com a chave (nome do prato) e o valor (preço do prato). No código original, havia um erro na iteração do dicionário, que foi corrigido, e a formatação da string também foi ajustada para refletir corretamente os valores.
'''
