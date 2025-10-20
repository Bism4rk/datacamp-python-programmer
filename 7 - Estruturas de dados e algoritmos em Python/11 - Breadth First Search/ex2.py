import queue

def bfs(graph, initial_vertex, search_value):
  visited_vertices = []
  bfs_queue = queue.SimpleQueue()
  visited_vertices.append(initial_vertex)
  bfs_queue.put(initial_vertex)

  while not bfs_queue.empty():
    current_vertex = bfs_queue.get()
    # Check if you found the search value
    if current_vertex == search_value:
      # Return True if you find the search value
      return True    
    for adjacent_vertex in graph[current_vertex]:
      # Check if the adjacent vertex has been visited
      if adjacent_vertex not in visited_vertices:
        visited_vertices.append(adjacent_vertex)
        bfs_queue.put(adjacent_vertex)
  # Return False if you didn't find the search value
  return False

print(bfs(graph, '4', '8')) # type: ignore // Assume graph is defined elsewhere, which doesn't matter for this example

'''
O código acima demonstra como implementar o algoritmo de busca em largura (BFS) em Python. Ele utiliza uma fila para explorar os vértices de um grafo de forma sistemática, começando por um vértice inicial e procurando por um valor específico. O algoritmo marca os vértices visitados para evitar ciclos e garante que todos os vértices adjacentes sejam explorados antes de avançar para o próximo nível do grafo. Se o valor de busca for encontrado, a função retorna True; caso contrário, retorna False após explorar todos os vértices acessíveis a partir do vértice inicial. Pesquisas BFS são amplamente utilizadas em várias aplicações, como na busca de caminhos em grafos, na análise de redes sociais e na resolução de problemas de labirintos,  e são diferentes de outras técnicas de busca, como a busca em profundidade (DFS), que explora o grafo de maneira mais profunda antes de voltar para explorar outros caminhos.
'''
