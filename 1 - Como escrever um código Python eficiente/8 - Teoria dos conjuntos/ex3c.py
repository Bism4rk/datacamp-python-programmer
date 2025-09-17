from ex3 import find_unique_items, names, primary_types, generations

# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types) 
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n') 

'''
O código acima demonstra duas abordagens para coletar nomes únicos de Pokémon: uma usando uma função personalizada e outra usando um conjunto. Ambas as abordagens devem produzir resultados equivalentes. Porém, a abordagem usando conjuntos é geralmente mais eficiente e concisa.
'''