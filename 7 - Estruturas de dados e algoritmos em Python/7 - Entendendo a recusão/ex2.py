def hanoi(num_disks, from_rod, to_rod, aux_rod):
  # Correct the base case
  if num_disks >= 1:
    # Correct the calls to the hanoi function
    hanoi(num_disks - 1, from_rod, aux_rod, to_rod)
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks -1, aux_rod, to_rod, from_rod)   

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)

'''
O código acima demonstra a solução do problema das Torres de Hanoi usando recursão em Python. A função 'hanoi' é definida para mover um número especificado de discos de uma haste de origem para uma haste de destino, utilizando uma haste auxiliar. A base da recursão é corrigida para garantir que a função só execute movimentos quando houver pelo menos um disco para mover (num_disks >= 1). A função faz chamadas recursivas para mover os discos menores para a haste auxiliar, move o disco maior diretamente para a haste de destino e, em seguida, move os discos menores da haste auxiliar para a haste de destino. O resultado é uma sequência de movimentos que resolve o problema das Torres de Hanoi para o número especificado de discos.
'''