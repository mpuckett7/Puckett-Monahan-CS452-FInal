import sys

#Find out if a given set of vertices is a clique
def is_clique(u, v, vertices, edges):

    #loop over all possible edges between vertices
    for i in range(u, v):
        for j in range(u + 1, v):
            
            #if an edge is missing then return false
            if(edges[vertices.get(i)][vertices.get(j)] == 0):
                return False
    
    return True


def max_cliques(vertices, edges):

    mc = 0

    #number of vertices
    num_v = len(vertices.keys())

    #check every vertex eventually
    for i in range(1, num_v + 1):

        if (is_clique(i, i, vertices, edges)):

            mc = max(mc, i)

            mc = max(mc, max_cliques(i, i + 1, vertices, edges))

    return mc


if name == '__main__':
    file_name = sys.argv[1]

    vertices = {}
    num_edges = 0
    edges = [[0 for i in range(num_edges)] for j in range(num_edges)]

    with open(file_name, "r") as file:
        for line in file:
            if num_edges == 0:
                num_edges = int(line.strip())
            else
                if str[0] in vertices and str[2] in vertices:
                    edges[vertices.get(str[0])][vertices.get(str[2])] = 1
                else if str[0] in vertices:
                    vertices[str[2]] = (str[2].ord() % 64)
                    edges[vertices.get(str[0])][vertices.get(str[2])] = 1
                else if str[2] in vertices:
                    vertices[str[0]] = (str[0].ord() % 64)
                    edges[vertices.get(str[0])][vertices.get(str[2])] = 1
                else:
                    vertices[str[0]] = (str[0].ord() % 64)
                    vertices[str[2]] = (str[2].ord() % 64)
                    edges[vertices.get(str[0])][vertices.get(str[2])]
    
    max_cliques(vertices, edges)


        