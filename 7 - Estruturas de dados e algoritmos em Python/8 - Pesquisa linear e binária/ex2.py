def binary_search_recursive(ordered_list, search_value):
  # Define the base case
  if len(ordered_list) == 0:
    return False
  else:
    middle = len(ordered_list)//2
    # Check whether the search value equals the value in the middle
    if search_value == ordered_list[middle]:
        return True
    elif search_value < ordered_list[middle]:
        # Call recursively with the left half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
    else:
        # Call recursively with the right half of the list
        return  binary_search_recursive(ordered_list[middle+1:], search_value)
  
print(binary_search_recursive([1,5,8,9,15,20,70,72], 5))

'''
O código acima demonstra como criar um algoritmo de busca binária recursiva em Python. A função `binary_search_recursive` recebe uma lista ordenada e um valor de busca, retornando `True` se o valor for encontrado na lista e `False` caso contrário. O algoritmo funciona dividindo repetidamente a lista ao meio, comparando o valor de busca com o valor do meio, e chamando a si mesmo com a metade apropriada da lista até que o valor seja encontrado ou a lista esteja vazia.
'''