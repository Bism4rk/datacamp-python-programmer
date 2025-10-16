class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []
    def enqueue(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore
            self.tail = new_node
    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None



        if self.head == None:

            self.tail = None
      
    def has_elements(self):
        return len(self.items) > 0

class PrinterTasks:
  def __init__(self):
    self.queue = Queue()
      
  def add_document(self, document):
    # Add the document to the queue
    self.queue.enqueue(document)
      
  def print_documents(self):
    # Iterate over the queue while it has elements
    while self.queue.has_elements():
      # Remove the document from the queue
      print("Printing", self.queue.dequeue())

printer_tasks = PrinterTasks()
# Add some documents to print
printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")
# Print all the documents in the queue
printer_tasks.print_documents()

'''
O código acima implementa uma fila (queue) usando uma lista encadeada em Python. A classe Node representa um nó na lista, contendo um valor (data) e uma referência para o próximo nó (next). A classe Queue gerencia a fila, permitindo adicionar elementos no final (enqueue) e remover elementos do início (dequeue). A classe PrinterTasks utiliza a fila para gerenciar documentos a serem impressos, adicionando documentos à fila e imprimindo-os na ordem em que foram adicionados.
'''