from ex2 import names

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

'''
O código acima demonstra como usar a função map() para aplicar uma função a cada elemento de um iterável. Neste caso, a função str.upper é aplicada a cada nome na lista names, resultando em uma nova lista de nomes em maiúsculas. A função map() retorna um objeto map, que é um iterável. Para criar uma lista a partir desse objeto, usamos o unpacking.
'''