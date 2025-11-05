import sys

sys.setrecursionlimit(2000000)

class StronglyConnectedComponents:
    def __init__(self):
        pass
    
    def tarjan_scc(self, adj):
        n = len(adj)
        index = 0
        indices = [-1] * n
        lowlink = [0] * n
        onstack = [False] * n
        stack = []
        sccs = []
        
        def strongconnect(v):
            nonlocal index
            indices[v], lowlink[v] = index, index
            index += 1
            stack.append(v)
            onstack[v] = True
            
            for w in adj[v]:
                if indices[w] == -1:
                    strongconnect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif onstack[w]:
                    lowlink[v] = min(lowlink[v], indices[w])
            if lowlink[v] == indices[v]:
                comp = []
                while True:
                    w = stack.pop()
                    onstack[w] = False
                    comp.append(w)
                    if w == v:
                        break
                sccs.append(comp)

        for v in range(n):
            if indices[v] == -1:
                strongconnect(v)
        return sccs, len(sccs)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
