def dfs(visited_vertices, graph, current_vertex):
    # Check if current_vertex hasn't been visited yet
    if current_vertex not in visited_vertices:
        print(current_vertex)
        # Add current_vertex to visited_vertices
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            # Call recursively with the appropriate values
            dfs(visited_vertices, graph, adjacent_vertex)
            
dfs(set(), graph, '0') # type: ignore // Assuming graph is defined elsewhere


'''
O código acima demonstra como implementar a técnica de Depth First Search (DFS) para percorrer um grafo. A função `dfs` verifica se o vértice atual já foi visitado; se não, imprime o vértice, marca-o como visitado e chama a si mesma recursivamente para cada vértice adjacente. Isso resulta em uma travessia profunda do grafo, explorando o máximo possível ao longo de cada ramificação antes de retroceder. DFS em grafos é frequentemente utilizado em algoritmos de busca, resolução de labirintos e análise de conectividade em redes, e é diferente das travessias em árvores pois um grafo pode conter ciclos e múltiplos caminhos entre os vértices.
'''