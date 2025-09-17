from ex1 import ash_pokedex
brock_pokedex = ['Golem', 'Omastar', 'Geodude', 'Zubat', 'Kabutops', 'Tauros', 'Machop', 'Onix', 'Vulpix', 'Dugtrio']


# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

'''
O código acima demonstra como usar o operador `in` para verificar a presença de elementos em listas e conjuntos. Ele mostra a verificação da presença de 'Psyduck' e 'Machop' nas listas de Ash e nos conjuntos de Brock.
'''