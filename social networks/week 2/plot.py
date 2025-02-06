import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):
    all_degrees = list(dict(nx.degree(G)).values())
    unique_degrees = list(set(all_degrees))

    count_of_degrees = []
    
    for i in unique_degrees:
        x = all_degrees.count(i)
        count_of_degrees.append(x)

    plt.plot(unique_degrees,count_of_degrees, 'yo-')
    plt.xlabel('Degrees')
    plt.ylabel('Number of nodes')
    plt.title('Degree Distrubution')
    plt.show()