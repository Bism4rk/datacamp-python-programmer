def selection_sort(my_list):
  list_length = len(my_list)
  for i in range(list_length - 1):
    # Set lowest to the element of the list located at index i
    lowest = my_list[i]
    index = i
    # Iterate again over the list starting on the next position of the i variable
    for j in range(i+1, list_length):
      # Compare whether the element of the list located at index j is smaller than lowest
      if my_list[j] < lowest:
        index = j
        lowest = my_list[j]
    my_list[i] , my_list[index] = my_list[index] , my_list[i]
  return my_list

my_list = [6, 2, 9, 7, 4, 8] 
selection_sort(my_list)
print(my_list)

'''
O código acima demonstra como implementar o algoritmo de ordenação por seleção em Python. Ele percorre a lista, selecionando o menor elemento e trocando-o com o elemento atual. O processo é repetido até que toda a lista esteja ordenada. A complexidade de tempo do algoritmo é O(n²), onde n é o número de elementos na lista. A ordenação por seleção é um algoritmo simples, mas não é o mais eficiente para listas grandes. É mais adequado para listas pequenas ou quando a simplicidade do código é mais importante que a eficiência. A ordenação por seleção é um algoritmo in-place, o que significa que não requer espaço adicional significativo além da lista original.
'''