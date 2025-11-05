import os

import matplotlib.pyplot as plt

figsize=(7, 5)

def plot_histogram(type, adj, filename):
    if type == 'Degree':
        degrees = [len(u) for u in adj]
    elif type == 'OutDegree':
        degrees = [len(u[0]) for u in adj]
    elif type == 'InDegree':
        degrees = [len(u[1]) for u in adj]

    max_deg = max(degrees) if degrees else 0
    counts = [degrees.count(d) for d in range(max_deg + 1)]
    deg_list = [f"deg{d}:{c}" for d, c in enumerate(counts)]
    # print(type, '=', deg_list)

    plt.figure(figsize=figsize)
    bars = plt.bar(range(len(counts)), counts, edgecolor='black')
    plt.xticks(range(len(counts)))
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    filename = os.path.splitext(os.path.basename(filename))[0]
    plt.title(f'{type} Histogram of Graph :- {filename}')

    for rect, c in zip(bars, counts):
        plt.text(rect.get_x() + rect.get_width() / 2, c, str(c), ha='center', va='bottom')

    plt.show()


























