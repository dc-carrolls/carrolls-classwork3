import json

data = { 'A':{'B':3,'C':2}, 'B':{'C':4}, 'C':{'A':1}}

# Writing JSON data
with open('file-io/data.json', 'w') as f:
	json.dump(data, f)
	
	
# Reading data
with open('file-io/data.json', 'r') as f:
	data2 = json.load(f)
	
# Output Data
for node in data2:
  print('Node', node, 'Has child node(s)')
  for child_node in data2[node]:
    print(child_node, 'with edge weight', data2[node][child_node])
	

