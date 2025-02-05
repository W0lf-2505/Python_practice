import networkx as nx
import itertools

def communities_brute(G):
    nodes = G.nodes()
    n = G.number_of_nodes()

    first_community = []

    print((n/2)+1)
    for i in range(1,int((n/2)+1)):
        comb = [list(x) for x in itertools.combinations(nodes,i)]
        first_community.extend(comb)

    second_community = []

    
    #which division is the best?
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []

    ratio = [] # ratio of intra edges / inter edges
    for i in range(len(first_community)):
        l = list(set(nodes) - set(first_community[i]))
        second_community.append(l)
        num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())


    for i in range(len(second_community)):
        num_intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())

    e = G.number_of_edges()

    for i in range(len(first_community)):
        num_inter_edges.append(e - num_intra_edges1[i] - num_intra_edges2[i])

    
    for i in range(len(num_inter_edges)):
        ratio.append((float)(num_intra_edges1[i] + num_intra_edges2[i])/num_inter_edges[i])

    max_value = max(ratio)
    max_index = ratio.index(max_value)

    print('(',first_community[max_index],')','(',second_community[max_index],')')

    