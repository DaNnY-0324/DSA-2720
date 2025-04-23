from collections import deque

def course_schedule(n, prerequisites):
    adj_matrix = [[0] * n for _ in range(n)]
    for a, b in prerequisites:
        adj_matrix[b][a] = 1 
    
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                in_degree[j] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    if len(order) == n:
        return order
    else:
        return []
    
