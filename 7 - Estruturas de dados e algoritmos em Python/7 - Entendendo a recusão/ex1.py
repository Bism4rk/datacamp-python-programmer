def fibonacci(n):
  # Define the base case
  if n <= 1:
    return n
  else:
    # Call recursively to fibonacci
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))

# cache = [None]*(100)

# def fibonacci(n): 
#     if n <= 1:
#         return n
    
#     # Check if the value exists
#     if not cache[n]:
#         # Save the result in cache
#         cache[n] = fibonacci(n-1) + fibonacci(n-2)
    
#     return cache[n]
    

# print(fibonacci(6))

'''
O código acima demonstra duas maneiras de implementar a função de Fibonacci usando recursão em Python. A primeira implementação é uma abordagem direta e simples, onde a função chama a si mesma para calcular os dois termos anteriores da sequência até atingir o caso base (n <= 1). No entanto, essa abordagem pode ser ineficiente para valores maiores de n, pois recalcula os mesmos valores várias vezes. A segunda implementação utiliza memoização, armazenando os resultados já calculados em uma lista chamada 'cache'. Isso evita cálculos redundantes, melhorando significativamente a eficiência da função para valores maiores de n.
'''