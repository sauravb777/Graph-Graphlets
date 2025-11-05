from build_graph import BuildGraph
from connected_components import ConnectedComponents
from graphlet import Graphlet
from plot import plot_histogram
from scc import StronglyConnectedComponents

bg = BuildGraph()
scc_obj = StronglyConnectedComponents()
cc_obj = ConnectedComponents()
gl = Graphlet()

def main(filename):
    dg = bg.Directed_Graph(filename)
    sccs, scc_count = scc_obj.tarjan_scc(dg)
    print(f"{filename} SCC_count: {scc_count}")

    ug = bg.Undirected_Graph(filename)
    comps = cc_obj.connected_components(ug)
    print(f"{filename} Connected_components_count: {len(comps)}")

    two_paths = gl.two_paths_three_node(ug)
    triangles = gl.triangle_three_node(ug)
    graphlets3 = gl.graphlet_size_3(ug)
    # print(f"{filename} Two_path_3node: {two_paths} Triangles: {triangles} Graphlets_size_3: {graphlets3}")
    print(f"{filename} Total Graphlets of size 3: {graphlets3}")


    d2 = bg.Directed_2Sets_Graph(filename)
    
    plot_histogram('Degree', ug, filename)
    plot_histogram('InDegree', d2, filename)
    plot_histogram('OutDegree', d2, filename)

files = ['./graph/n10.txt', './graph/n100.txt', './graph/n1000.txt', './graph/n10000.txt', './graph/s1.txt']


for f in files:
    main(f)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
