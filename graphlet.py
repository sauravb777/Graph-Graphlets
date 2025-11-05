from math import comb


class Graphlet:
    def __init__(self):
        pass
    
    def two_paths_three_node(self, adj):
        total = 0
        for neighbors in adj:
            k = len(neighbors)
            if k >= 2:
                total += comb(k+1, 3)
        return total

    def triangle_three_node(self, adj):
        triangles_times3 = 0
        n = len(adj)
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    if len(adj[u]) < len(adj[v]):
                        small, large = adj[u], adj[v]
                    else:
                        small, large = adj[v], adj[u]
                    for w in small:
                        if w == u or w == v:
                            continue
                        if w in large:
                            triangles_times3 += 1
        return triangles_times3 // 3

    def graphlet_size_3(self, adj):
        t2 = self.two_paths_three_node(adj)
        t3 = self.triangle_three_node(adj)
        return t2 - 2 * t3












