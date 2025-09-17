# Import combinations from itertools
from itertools import combinations

pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)

'''
O código acima demonstra como usar a função `combinations` do módulo `itertools` para gerar combinações de elementos em uma lista. Ele cria combinações de pares e grupos de dois e quatro Pokémon a partir da lista `pokemon`. A função `combinations` é uma maneira eficiente de gerar combinações sem repetição, facilitando a análise de grupos de elementos.
'''