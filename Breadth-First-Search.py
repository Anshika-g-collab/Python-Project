graph = {
    '15' : ['13','17'],
    '13' : ['12','14'],
    '17' : ['18'],
    '12' : [],
    '14' : ['18'],
    '18' : []
}
visited = []
queue = []
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("Following is the Breadth-First Search")
bfs(visited,graph,'15')