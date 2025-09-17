names = ['Blaziken', 'Garchomp', 'Samurott', 'Koraidon', 'Aggron', 'Feraligatr', 'Lugia', 'Decidueye', 'Zacian', 'Blaziken', 'Garchomp', 'Samurott', 'Koraidon', 'Aggron', 'Feraligatr', 'Lugia', 'Decidueye', 'Zacian', 'Blaziken', 'Garchomp', 'Samurott', 'Koraidon', 'Aggron', 'Feraligatr', 'Lugia', 'Decidueye', 'Zacian']
primary_types = ['Fire', 'Dragon', 'Water', 'Dragon', 'Steel', 'Water', 'Psychic', 'Grass', 'Fairy', 'Fire', 'Dragon', 'Water', 'Dragon', 'Steel', 'Water', 'Psychic', 'Grass', 'Fairy', 'Fire', 'Dragon', 'Water', 'Dragon', 'Steel', 'Water', 'Psychic', 'Grass', 'Fairy']
generations = [3, 4, 5, 9, 3, 2, 2, 7, 8, 3, 4, 5, 9, 3, 2, 2, 7, 8, 3, 4, 5, 9, 3, 2, 2, 7, 8]

def find_unique_items(data):
    uniques = []
    for item in data:
        if item not in uniques:
            uniques.append(item)
    return uniques

# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(uniq_names_func)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

'''
O código acima demonstra duas abordagens para coletar nomes únicos de Pokémon: uma usando uma função personalizada e outra usando um conjunto. Ambas as abordagens devem produzir resultados equivalentes.
'''