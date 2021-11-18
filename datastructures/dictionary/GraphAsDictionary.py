#OCR A Level Computer Science Unit 7 Topic 6 Graphs
#representing a graph (Worksheet 6 qu 4
#GraphAsDictionary.py
unweightedGraph = {'A':['B','D','E'],
    'B':['A','C','D'],
    'C':['B','G'],
    'D':['A','B','E','F'], 
    'E':['A','D'],
    'F':['D'],
    'G':['C']
   }



weightedGraph = {'A':{'B':5,'D':8,'E':4},
    'B':{'A':5,'C':4,'D':3},
    'C':{'B':4,'G':2},
    'D':{'A':8,'B':3,'E':7,'F':6}, 
    'E':{'A':4,'D':7},
    'F':{'D':6},
    'G':{'C':2}
   }




nodes = list(unweightedGraph['A'])
print(nodes)

nodes = list(weightedGraph['A'])
print(nodes)

