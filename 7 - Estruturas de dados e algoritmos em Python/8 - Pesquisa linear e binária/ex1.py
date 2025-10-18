def binary_search(ordered_list, search_value):
  first = 0
  last = len(ordered_list) - 1
  
  while first <= last:
    middle = (first + last)//2
    # Check whether the search value equals the value in the middle
    if search_value == ordered_list[middle]:
      return True
    # Check whether the search value is smaller than the value in the middle
    elif search_value < ordered_list[middle]:
      # Set last to the value of middle minus one
      last = middle - 1
    else:
      first = middle + 1
  return False
  
print(binary_search([1,5,8,9,15,20,70,72], 5))

'''
O código acima demonstra como criar um algoritmo de busca binária em Python. A função `binary_search` recebe uma lista ordenada e um valor de busca, retornando `True` se o valor for encontrado na lista e `False` caso contrário. O algoritmo funciona dividindo repetidamente a lista ao meio, comparando o valor de busca com o valor do meio, e ajustando os limites de busca conforme necessário até que o valor seja encontrado ou os limites se cruzem.
'''