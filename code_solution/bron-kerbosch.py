#Based on the Bron-Kerbosch Algorithm without Pivoting or Vertex Ordering
#Citation: Wikipedia https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
#https://gist.github.com/abhin4v/8304062 which is in the wiki pages external links

# Written By: Mason Puckett and Annabelle Monahan
import sys
from datetime import datetime
from collections import defaultdict

#graph is based on adjacency list
#vertices being keys with a list of neighbors for values
def find_cliques(graph):
    p = set(graph.keys())
    r = set()
    x = set()
    cliques = []

    bron_kerbosch1(r, p, x, cliques, graph)

    return sorted(cliques, key=len)

#Does reporting of cliques and set manipulation
#Basic version based off of wiki page
def bron_kerbosch1(R, P, X, cliques, graph):
    if len(P) == 0 and len(X) == 0:
        cliques.append(R)
    else:
        for v in P.copy():
            neighbors = graph[v]
            bron_kerbosch1(R.union([v]), P.intersection(neighbors), X.intersection(neighbors), cliques, graph)
            P.remove(v)
            X.add(v)


if __name__ == '__main__':

    vertices = {}
    num_edges = 0
    edges = []

    now = datetime.now()
    curr_time = now.strftime("%H: %M: %S")
    print("Current time = ", curr_time)
    file_name = sys.argv[1]
    alphabet_map = {chr(i + 96): i for i in range(1, 27)}

    with open("./test_cases/" + file_name, "r") as file:
        for line in file:
            if (num_edges == 0):
                num_edges = int(line.strip())
                edges = [[0 for i in range(num_edges)] for j in range(num_edges)]
            else:
                if (line[0] in vertices and line[2] in vertices):
                    edges[vertices.get(line[0])][vertices.get(line[2])] = 1
                    edges[vertices.get(line[2])][vertices.get(line[0])] = 1
                elif (line[0] in vertices):
                    vertices[line[2]] = alphabet_map[line[2]]
                    edges[vertices.get(line[0])][vertices.get(line[2])] = 1
                    edges[vertices.get(line[2])][vertices.get(line[0])] = 1
                elif (line[2] in vertices):
                    vertices[line[0]] = alphabet_map[line[0]]
                    edges[vertices.get(line[0])][vertices.get(line[2])] = 1
                    edges[vertices.get(line[2])][vertices.get(line[0])] = 1
                else:
                    vertices[line[0]] = alphabet_map[line[0]]
                    vertices[line[2]] = alphabet_map[line[2]]
                    edges[vertices.get(line[0])][vertices.get(line[2])] = 1
                    edges[vertices.get(line[2])][vertices.get(line[0])] = 1

    graph = {}

    for v in vertices.keys():
        neighbors = []
        for i in range(1, len(edges[vertices[v]])):
            if edges[vertices[v]][i] == 1:
                neighbors.append(i)

        graph[vertices[v]] = neighbors

    cliques = find_cliques(graph)

    now = datetime.now()
    curr_time = now.strftime("%H: %M: %S")
    print("Current time = ", curr_time)

    print(len(cliques[0]))
