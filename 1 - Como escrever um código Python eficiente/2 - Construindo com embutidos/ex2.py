names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)

'''
O código acima demonstra como usar a função enumerate() para obter pares de índice e valor ao iterar sobre uma lista. A primeira abordagem usa um loop for tradicional, enquanto a segunda abordagem utiliza compreensão de listas para criar a mesma lista de tuplas de forma mais concisa. A terceira abordagem mostra como desempacotar um objeto enumerate com um índice inicial de um.
'''