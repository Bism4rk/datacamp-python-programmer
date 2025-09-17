names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl']
primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', 'Rock']
secondary_types = ['Ice', None, None, None, 'Flying']

# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine all three lists together
names_types = list(zip(names, primary_types, secondary_types))

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')

'''
O código acima demonstra como combinar listas de forma eficiente usando a função `zip`. Ele combina os nomes dos Pokémon com seus tipos primários e secundários, e também mostra como lidar com listas de tamanhos diferentes. A função `zip` é uma maneira eficiente de iterar sobre múltiplas listas simultaneamente, criando tuplas que contêm elementos correspondentes de cada lista.
'''