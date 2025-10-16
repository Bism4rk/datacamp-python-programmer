# Import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")

# Remove an element from the stack
my_book_stack.get()

'''
O código acima demonstra como utilizar a classe `LifoQueue` do módulo `queue` em Python para implementar uma pilha (stack) com comportamento LIFO (Last In, First Out). A pilha é criada com tamanho infinito, permitindo adicionar e remover elementos conforme necessário. A função `put` é usada para adicionar um elemento ao topo da pilha, enquanto a função `get` remove e retorna o elemento do topo.
'''