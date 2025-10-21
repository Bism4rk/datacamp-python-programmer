'''
Código original com erros:
def merge_sort(my_list):
    if len(my_list) > 1: 
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
 
        i = j = k = 0
 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
        		# Correct mistake when assigning left half
                my_list[k] = right_half[i]                
                i += 1
            else:
                # Correct mistake when assigning right half
                my_list[k] = left_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            my_list[k] = left_half[i]
            # Correct mistake when updating pointer for left half
            j += 1
            k += 1
 
        while j < len(right_half):
            my_list[k] = right_half[j]
            # Correct mistake when updating pointer for right half
            i += 1
            k += 1

my_list = [35,22,90,4,50,20,30,40,1]
merge_sort(my_list)
print(my_list)
'''

def merge_sort(my_list):
    if len(my_list) > 1: 
        mid = len(my_list)//2
        left_half = my_list[mid:]
        right_half = my_list[:mid]
        
        merge_sort(left_half)
        merge_sort(right_half)
 
        i = j = k = 0
 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
        		# Correct mistake when assigning left half
                my_list[k] = left_half[i]                
                i += 1
            else:
                # Correct mistake when assigning right half
                my_list[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            my_list[k] = left_half[i]
            # Correct mistake when updating pointer for left half
            i += 1
            k += 1
 
        while j < len(right_half):
            my_list[k] = right_half[j]
            # Correct mistake when updating pointer for right half
            j += 1
            k += 1

my_list = [35,22,90,4,50,20,30,40,1]
merge_sort(my_list)
print(my_list)

'''
O código acima demonstra como implementar o algoritmo de ordenação por mesclagem (merge sort) em Python. Ele corrige os erros presentes no código original, garantindo que a lista seja dividida corretamente em metades, e que os elementos sejam comparados e mesclados de forma adequada para produzir uma lista ordenada. Os erros eram:
1. A divisão da lista em `left_half` e `right_half` estava invertida.
2. Durante a mesclagem, os elementos estavam sendo atribuídos incorretamente às posições da lista original.
3. Os ponteiros `i` e `j` não estavam sendo atualizados corretamente nas etapas finais de mesclagem.

Ordenação por mesclagem é um algoritmo eficiente com complexidade de tempo O(n log n) e é amplamente utilizado devido à sua estabilidade e eficiência em grandes conjuntos de dados. Porém, sua complexidade de espaço é O(n) devido ao uso de listas auxiliares para armazenar as metades da lista original, ao contrário de outros algoritmos como o bubble sort, que possuem complexidade de espaço O(1). Por isso, a escolha do algoritmo de ordenação deve considerar tanto a eficiência temporal quanto a espacial, dependendo do contexto e dos requisitos específicos da aplicação.
'''