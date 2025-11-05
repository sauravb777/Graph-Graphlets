class BuildGraph:
    def __init__(self):
        pass

    def Directed_Graph(self, filename):
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            adj = [set() for _ in range(n)]
            for line in file:
                line = line.strip()
                if not line:
                    continue
                u, v = map(int, line.split())
                adj[u].add(v)
        return adj

    def Undirected_Graph(self, filename):
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            adj = [set() for _ in range(n)]
            for line in file:
                line = line.strip()
                if not line:
                    continue
                u, v = map(int, line.split())
                adj[u].add(v)
                adj[v].add(u)
        return adj

    def Directed_2Sets_Graph(self, filename):
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            adj = [[set(), set()] for _ in range(n)]
            for line in file:
                line = line.strip()
                if not line:
                    continue
                u, v = map(int, line.split())
                adj[u][0].add(v)
                adj[v][1].add(u)
        return adj

















