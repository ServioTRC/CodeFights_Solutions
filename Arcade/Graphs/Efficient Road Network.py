import queue  

def minEdgeBFS(edges, u, v, n): 
      
    visited = [0] * n  
    distance = [0] * n 
    Q = queue.Queue() 
    distance[u] = 0
  
    Q.put(u)  
    visited[u] = True
    while (not Q.empty()): 
        x = Q.get()  
        for i in range(len(edges[x])): 
            if (visited[edges[x][i]]): 
                continue
            distance[edges[x][i]] = distance[x] + 1
            Q.put(edges[x][i])  
            visited[edges[x][i]] = 1
    return distance[v] 
  
def addEdge(edges, u, v): 
    edges[u].append(v)  
    edges[v].append(u) 
  
def efficientRoadNetwork(n, roads):
    edges = [[] for i in range(n)]
    for road in roads:
        addEdge(edges, road[0], road[1])
    matrix = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if not matrix[i][j] or not matrix[j][i]:
                val = minEdgeBFS(edges, i, j, n)
                if val > 2 or val == 0:
                    return False
                matrix[i][j] = True
                matrix[j][i] = True
    return True

roads = [[0, 1], [0, 2], [3, 4]]

print(efficientRoadNetwork(5, roads))