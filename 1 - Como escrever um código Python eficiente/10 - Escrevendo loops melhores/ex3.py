names = ['Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Treecko', 'Grovyle', 'Sceptile', 'Poochyena', 'Mightyena', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock']
hps = [50, 70, 90, 50, 70, 100, 50, 65, 80, 35, 70, 90, 73, 70, 70]

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')

'''
O código acima demonstra como melhorar loops utilizando a biblioteca NumPy para calcular a média e o desvio padrão de forma mais eficiente. Além disso, a utilização de list comprehensions permite filtrar os Pokémon com base em suas pontuações Z de maneira mais concisa e legível.
'''