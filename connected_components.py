class ConnectedComponents:
    def __init__(self):
        pass

    def connected_components(self, adj):
        n = len(adj)
        visited = [False] * n
        components = []

        def dfs(u, comp):
            visited[u] = True
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    dfs(v, comp)

        for u in range(n):
            if not visited[u]:
                comp = []
                dfs(u, comp)
                components.append(comp)

        return components








