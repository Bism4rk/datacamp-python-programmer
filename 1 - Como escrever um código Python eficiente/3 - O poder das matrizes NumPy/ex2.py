import numpy as np

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

def welcome_guest(guest):
    name, arrival_time = guest
    return f"Welcome {name}! You arrived {arrival_time} min late."

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

'''
O código acima demonstra como usar o NumPy para manipular dados de forma eficiente. Ele mostra como criar um array a partir de uma lista, realizar operações vetorizadas e aplicar funções a elementos de forma concisa. Além disso, ilustra como combinar programação funcional com estruturas de dados eficientes. A lista de tempos `arrival_times` é convertida em um array NumPy, e então os tempos são atualizados de forma vetorizada. Depois disso, a lista de chegadas dos convidados é criada usando compreensão de lista e `enumerate`, e a função `welcome_guest` é aplicada a cada par (convidado, tempo) usando `map`.
'''