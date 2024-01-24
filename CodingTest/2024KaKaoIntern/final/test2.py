from collections import defaultdict

def create_graph(edges):
    graph = defaultdict(set)
    for edge in edges:
        from_n, to_n = edge[0], edge[1]
        graph[from_n].add(to_n)
    return graph

def find_max(graph):
    max_edge = 0
    dot = -1
    for vertex, edges in graph.items():
        edge_num = len(edges)
        if edge_num > max_edge: 
            max_edge = edge_num
            dot = vertex
    return dot

def find_graph_type(graph, dot):
    graph_type = [0, 0, 0]

    for d in graph[dot]:
        vertex_cnt = 0
        edge_cnt = 0

        visited = set()
        stack = [d]

        while stack:
            current = stack.pop()
            
            if current not in visited:
                visited.add(current)
                vertex_cnt += 1
                
                if current in graph:
                    edge_cnt += len(graph[current])
                    
                    for next_dot in graph[current]:
                        if next_dot not in visited:
                            stack.append(next_dot)

        if vertex_cnt == edge_cnt:
            graph_type[0] += 1 
        elif edge_cnt == vertex_cnt - 1:
            graph_type[1] += 1
        else:
            graph_type[2] += 1
    
    return graph_type

def solution(edges):
    graph = create_graph(edges)
    cnt_max_dot = find_max(graph)
    graph_type = find_graph_type(graph, cnt_max_dot)

    answer = [cnt_max_dot]
    answer += graph_type

    return answer

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(edges))