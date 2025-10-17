class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex):
    self.vertices[vertex] = []

  def add_edge(self, source, target):
    self.vertices[source].append(target)

class WeightedGraph:
  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex):
    # Set the data for the vertex
    self.vertices[vertex] = []
    
  def add_edge(self, source, target, weight):
    # Set the weight
    self.vertices[source].append([target, weight])

my_graph = WeightedGraph()

# Create the vertices
my_graph.add_vertex('Paris')
my_graph.add_vertex('Toulouse')
my_graph.add_vertex('Biarritz')

# Create the edges
my_graph.add_edge('Paris', 'Toulouse', 678)
my_graph.add_edge('Toulouse', 'Biarritz', 312)
my_graph.add_edge('Biarritz', 'Paris', 783)

'''
O código acima demonstra como criar uma estrutura básica de grafo ponderado em Python. A classe WeightedGraph permite adicionar vértices e arestas com pesos associados. As arestas são representadas como listas que contêm o vértice de destino e o peso da aresta, facilitando a representação de grafos onde as conexões entre os nós têm custos ou distâncias associadas. Essa estrutura é útil para modelar redes como rotas de transporte, onde diferentes caminhos podem ter diferentes distâncias ou tempos de viagem. No caso, o grafo representa cidades conectadas por estradas com distâncias específicas.
'''