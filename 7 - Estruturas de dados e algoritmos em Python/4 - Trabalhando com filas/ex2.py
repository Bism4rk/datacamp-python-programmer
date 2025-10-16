import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")

# Remove an element from the queue
my_orders_queue.get()

'''
O código acima demonstra como criar e utilizar uma fila (queue) em Python usando o módulo queue. Ele cria uma fila simples, adiciona um elemento ("samosas") à fila e, em seguida, remove esse elemento da fila. Filas são estruturas de dados que seguem o princípio FIFO (First In, First Out), onde o primeiro elemento adicionado é o primeiro a ser removido.
'''