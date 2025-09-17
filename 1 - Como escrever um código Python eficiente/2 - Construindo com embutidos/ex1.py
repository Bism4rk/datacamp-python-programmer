# Create a range object that goes from 0 to 5
nums = range(0,6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,13,2)]
print(nums_list2)

'''
O código acima demonstra como usar diferentes funções embutidas em Python, como range(), list() e unpacking. Essas funções ajudam a criar e manipular listas de forma eficiente e concisa. A lista `nums` é criada usando a função `range()`, que gera uma sequência de números. Em seguida, a lista é convertida em uma lista real usando a função `list()`. Por fim, uma nova lista de números ímpares é criada usando unpacking.
'''