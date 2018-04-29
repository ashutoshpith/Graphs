graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
def generate_edges_graph(graph):
    edges = []
    for node in graph:
        for side in graph[node]:
            edges.append((node, side))

    return edges

print(generate_edges_graph(graph))

def find_isolated_nodes_graph(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

print(find_isolated_nodes_graph(graph))
