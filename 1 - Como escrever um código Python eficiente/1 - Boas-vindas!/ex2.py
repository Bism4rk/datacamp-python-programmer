names = ["Alice", "Bob", "Charlie", "David", "Edward", "Fiona", "Christopher", "Jonathan"]

# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)

'''
O código acima demonstra diferentes abordagens para filtrar uma lista de nomes com base no comprimento do nome. A abordagem não-pytonica usa um loop while, a abordagem intermediaria usa um loop for, e a melhor abordagem utiliza compreensão de listas. Abordagens mais eficientes geralmente resultam em código mais limpo e legível.
'''