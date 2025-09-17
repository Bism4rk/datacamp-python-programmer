from collections import Counter

names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aipom']
primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', 'Rock', 'Normal']
secondary_types = ['Ice', None, None, None, 'Flying', 'Fighting']
generations = [4, 3, 3, 5, 6, 2]

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

'''
O código acima demonstra como usar a classe `Counter` do módulo `collections` para contar ocorrências de elementos em listas. Ele conta os tipos primários dos Pokémon, as gerações e as letras iniciais dos nomes dos Pokémon. A classe `Counter` é uma maneira eficiente de realizar contagens e análises estatísticas simples em coleções de dados.
'''