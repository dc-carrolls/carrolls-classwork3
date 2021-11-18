#dfs.py depth first graph traversal

# note that constants are customarily given names all in uppercase
GRAPH = {
    'A':['B','D','E'],
    'B':['A','C','D'],
    'C':['B','G'],
    'D':['A','B','E','F'],
    'E':['A','D'],
    'F':['D'],
    'G':['C']}

visitedList = []

def dfs(graph, currentVertex, visited):

    print('Visit', currentVertex, ' and add to visited list')
    visited.append(currentVertex)
    print('List of visited nodes:',visited)
    for vertex in graph[currentVertex]:

        print('  Checking neighbour', vertex)

        if vertex not in visited:
            print('\nPush ', currentVertex,' onto stack')
            dfs(graph,vertex,visited)
            
            print('Pop', currentVertex,'off the stack')
        # end if
    # end for
    print('  All neighbours of', currentVertex, 'have been visited')
    return (visited)
# endsub dfs

#main

traversal = dfs(GRAPH,'A', visitedList)
print(traversal)

