import sys
from datetime import datetime

vertices = {}
num_edges = 0
edges = []

#Find out if a given set of vertices is a clique
def is_clique(t):

    #loop over all possible edges between vertices
    for i in range(1, t):
        for j in range(i + 1, t):
            
            #if an edge is missing then return false
            if(edges[vertices.get(chr(i + 96))][vertices.get(chr(j + 96))] == 0):
                return False
    
    return True


def max_cliques(s, e):

    mc = 0

    #number of vertices
    num_v = len(vertices.keys())

    #check every vertex eventually
    for i in range(s, num_v):
        # Add current vertex to potential clique
        if is_clique(e):
            mc = max(mc, e)
            mc = max(mc, max_cliques(i + 1, e + 1))

    return mc


if __name__ == '__main__':
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

    
    mc = max_cliques(0, 1)
    now = datetime.now()
    curr_time = now.strftime("%H: %M: %S")
    print("Current time = ", curr_time)
    print(mc)


        