poke_names = ['Charizard', 'Typhlosion', 'Blaziken', 'Infernape','Emboar','Delphox', 'Incineroar', 'Cinderace', 'Skeledirge']
poke_gens = [1, 2, 3, 4, 5, 6, 7, 8, 9]

gen1_gen2_name_lengths_loop = []

for name,gen in zip(poke_names, poke_gens):

    if gen < 3:

        name_length = len(name)

        poke_tuple = (name, name_length)

        gen1_gen2_name_lengths_loop.append(poke_tuple)

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

'''
O código acima demonstra como eliminar loops desnecessários utilizando compreensão de listas e a função map. Em vez de iterar sobre os Pokémon e calcular os comprimentos dos nomes em um loop, podemos fazer isso de forma mais concisa e eficiente. No caso, utilizamos a função map para aplicar a função len a cada elemento da lista gen1_gen2_pokemon, obtendo assim os comprimentos dos nomes de forma direta.
'''