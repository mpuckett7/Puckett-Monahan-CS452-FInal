#Approximation Algorithm based on Fiege's
#Citations: chatgpt for psuedocode because theres a pay wall at a journal database
#Wikipedia- clique problem/maximum clique

import sys
from datetime import datetime
import random
from collections import defaultdict



def fiege_max_clique_approx(graph, iterations=1000):

    best_clique = set()
    vertices = list(graph.keys())

    for _ in range(iterations):

        #shuffle the vertices 
        random.shuffle(vertices)
        curr_clique = set()

        for v in vertices:
            #check if v is connected to every vertex in the current clique
            if all(neighbor in graph[v] for neighbor in curr_clique):
                curr_clique.add(v)

        #update best_clique if the size of the current clique is greater
        if len(curr_clique) > len(best_clique):
            best_clique = curr_clique
    
    return list(best_clique)



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

    max_clique = fiege_max_clique_approx(graph)

    now = datetime.now()
    curr_time = now.strftime("%H: %M: %S")
    print("Current time = ", curr_time)

    print(len(max_clique))