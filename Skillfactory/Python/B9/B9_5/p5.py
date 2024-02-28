def dfs(visited, graph, stack, node):

    stack.append(node)
    print("Добавили в стек", node)
    print("Стек", stack)
    if node not in visited:
        print("Помечаем", node, "как посещенную")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, stack, neighbor)
        print("Убрать из стека", stack.pop(0))
        print("Стек", stack)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

stack = []
visited = set()
dfs(visited, graph, stack, "A")




