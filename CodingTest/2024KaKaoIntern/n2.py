###############################################################

from collections import defaultdict

def create_graph(edges):
    graph = defaultdict(set)
    for edge in edges:
        from_node, to_node = edge[0], edge[1]
        graph[from_node].add(to_node)
    return graph

def find_max(graph):
    max_edges = 0
    cnt_max = -1
    for vertex, edges in graph.items():
        edge_count = len(edges)
        if edge_count > max_edges:
            max_edges = edge_count
            cnt_max = vertex
    return [cnt_max]

def find_graph_type(graph, cnt_max):
    graph_type_counts = [0, 0, 0]

    for neighbor in graph[cnt_max]:
        vertex_count = 0
        edge_count = 0

        visited = set()
        stack = [neighbor]

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                vertex_count += 1

                if current in graph:
                    edge_count += len(graph[current])
                    for adjacent in graph[current]:
                        if adjacent not in visited:
                            stack.append(adjacent)

        if vertex_count == edge_count:
            graph_type_counts[0] += 1
        elif edge_count == vertex_count - 1:
            graph_type_counts[1] += 1
        else:
            graph_type_counts[2] += 1

    return graph_type_counts

def solution(edges):
    graph = create_graph(edges)
    cnt_max = find_max(graph)
    graph_types = find_graph_type(graph, cnt_max[0])

    # graph_types의 모든 요소를 answer 리스트에 추가
    answer = cnt_max + graph_types

    return answer
