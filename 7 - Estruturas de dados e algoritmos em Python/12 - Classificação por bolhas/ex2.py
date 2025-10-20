'''
Código original com erros:
def bubble_sort(my_list):
  list_length = len(my_list)
  # Correct the mistake
  is_sorted = True
  while not is_sorted:
    is_sorted = True
    for i in range(list_length-1):
      # Correct the mistake
      if my_list[i] < my_list[i+1]:
        my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
        is_sorted = False
    # Correct the mistake
    list_length += 1
  return my_list

print(bubble_sort([5, 7, 9, 1, 4, 2]))
'''


def bubble_sort(my_list):
  list_length = len(my_list)
  # Correct the mistake
  is_sorted = False
  while not is_sorted:
    is_sorted = True
    for i in range(list_length-1):
      # Correct the mistake
      if my_list[i] > my_list[i+1]:
        my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
        is_sorted = False
    # Correct the mistake
    list_length -= 1
  return my_list

print(bubble_sort([5, 7, 9, 1, 4, 2]))

'''
O código acima demonstra como implementar o algoritmo de ordenação por bolhas (bubble sort) em Python. Ele corrige os erros presentes no código original, garantindo que a lista seja ordenada corretamente em ordem crescente. Os erros eram: 
1. A variável `is_sorted` deve ser inicializada como `False` para entrar no loop.
2. A condição de comparação deve ser `if my_list[i] > my_list[i+1]:` para ordenar em ordem crescente.
3. O comprimento da lista deve ser decrementado (`list_length -= 1`) a cada iteração, já que o maior elemento "bolha" para o final da lista a cada passagem.

Bubble sort é um algoritmo simples, mas não é o mais eficiente para listas grandes nem para listas altamente desordenadas. Porém, é útil para entender os conceitos básicos de ordenação. Ele funciona comparando pares adjacentes de elementos e trocando-os se estiverem na ordem errada, repetindo esse processo até que a lista esteja ordenada.
'''