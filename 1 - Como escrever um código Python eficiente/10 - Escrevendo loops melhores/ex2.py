from itertools import combinations

pokemon_types = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

'''
O código acima demonstra como melhorar a eficiência de um loop utilizando a função combinations da biblioteca itertools para gerar todos os pares possíveis de tipos de Pokémon. Em seguida, utilizamos a função enumerate para adicionar um índice a cada par, criando uma lista de tuplas enumeradas. Por fim, convertemos todas as tuplas em listas, resultando em uma lista de pares enumerados.
'''