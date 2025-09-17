# Import Counter
from collections import Counter

generations = [1, 1, 2, 3, 4, 5, 5, 5,  6, 7, 8, 8, 9, 5, 6, 3, 2, 4]

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
    
'''
O código acima demonstra como melhorar a eficiência de um loop utilizando a biblioteca Counter para contar as gerações de Pokémon. Além disso, ao mover o cálculo do total de gerações para fora do loop, conseguimos evitar a repetição desse cálculo em cada iteração, resultando em um código mais eficiente.
'''